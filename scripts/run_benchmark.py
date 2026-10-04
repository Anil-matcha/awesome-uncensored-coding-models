#!/usr/bin/env python3
"""Run the benchmark prompts against a tool-capable Muapi text model."""

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "benchmark" / "tasks.jsonl"
DEFAULT_BASE_URL = "https://api.muapi.ai/v1"


def slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-.") or "model"


def api_request(url: str, api_key: str, body: dict | None = None):
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8") if body is not None else None,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST" if body is not None else "GET",
    )
    with urllib.request.urlopen(request, timeout=600) as response:
        return json.load(response)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Exact model ID from Muapi's text-model list")
    parser.add_argument("--runs", type=int, default=1, help="Repetitions per task (default: 1)")
    parser.add_argument("--max-tokens", type=int, default=1024)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument(
        "--allow-no-tools",
        action="store_true",
        help="Allow a model without tool support for a text-only comparison",
    )
    args = parser.parse_args()
    if args.runs < 1:
        parser.error("--runs must be at least 1")
    if args.max_tokens < 1:
        parser.error("--max-tokens must be at least 1")

    api_key = os.environ.get("MUAPI_API_KEY")
    if not api_key:
        print("Set MUAPI_API_KEY in your environment; the key is never written to results.", file=sys.stderr)
        return 2
    base_url = os.environ.get("MUAPI_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
    if not base_url.endswith("/v1"):
        print("MUAPI_BASE_URL must be the API root ending in /v1 (for example https://api.muapi.ai/v1).", file=sys.stderr)
        return 2

    try:
        model_payload = api_request(f"{base_url}/models?type=text", api_key)
        model_info = next(
            (item for item in model_payload.get("data", []) if item.get("id") == args.model),
            None,
        )
        if model_info is None:
            print(f"Unknown model ID {args.model!r}; select an ID from {base_url}/models?type=text.", file=sys.stderr)
            return 2
        supports_tools = bool((model_info.get("capabilities") or {}).get("tools"))
        if not supports_tools and not args.allow_no_tools:
            print(f"{args.model} does not advertise tool support; select a tool-capable model or pass --allow-no-tools.", file=sys.stderr)
            return 2
        tasks = [json.loads(line) for line in TASKS.read_text().splitlines() if line.strip()]
    except urllib.error.HTTPError as exc:
        print(f"Muapi request failed ({exc.code}): {exc.read().decode('utf-8', 'replace')[:500]}", file=sys.stderr)
        return 2
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"Could not load Muapi models or benchmark tasks: {exc}", file=sys.stderr)
        return 2

    output_dir = ROOT / "results"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{slug(args.model)}.jsonl"
    count = 0
    with output_path.open("a", encoding="utf-8") as out:
        for task in tasks:
            for run in range(1, args.runs + 1):
                seed = args.seed + run - 1
                body = {
                    "model": args.model,
                    "messages": [{"role": "user", "content": task["prompt"]}],
                    "max_tokens": args.max_tokens,
                    "temperature": args.temperature,
                    "seed": seed,
                }
                started = time.monotonic()
                record = {
                    "task_id": task["id"],
                    "task_version": task["version"],
                    "category": task["category"],
                    "safety": task["safety"],
                    "run": run,
                    "model_id": args.model,
                    "api_base_url": base_url,
                    "model_capabilities": model_info.get("capabilities", {}),
                    "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                    "temperature": args.temperature,
                    "seed": seed,
                    "max_tokens": args.max_tokens,
                    "prompt": task["prompt"],
                }
                try:
                    payload = api_request(f"{base_url}/chat/completions", api_key, body)
                    choices = payload.get("choices") or []
                    choice = choices[0] if choices else {}
                    message = choice.get("message") or {}
                    record.update(
                        {
                            "response_id": payload.get("id"),
                            "model_returned": payload.get("model"),
                            "response": message.get("content", ""),
                            "finish_reason": choice.get("finish_reason"),
                            "usage": payload.get("usage", {}),
                            "elapsed_seconds": round(time.monotonic() - started, 3),
                        }
                    )
                    print(f"{task['id']} run {run}: captured")
                except urllib.error.HTTPError as exc:
                    record.update(
                        {
                            "error_status": exc.code,
                            "error": exc.read().decode("utf-8", "replace")[:1000],
                            "elapsed_seconds": round(time.monotonic() - started, 3),
                        }
                    )
                    print(f"{task['id']} run {run}: API error {exc.code}", file=sys.stderr)
                except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                    record.update({"error": str(exc), "elapsed_seconds": round(time.monotonic() - started, 3)})
                    print(f"{task['id']} run {run}: request error {exc}", file=sys.stderr)
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
                out.flush()
                count += 1
    print(f"Wrote {count} records to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
