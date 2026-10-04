#!/usr/bin/env python3
"""Run the prompt set against a model served by a local Ollama instance."""

import argparse
import datetime as dt
import json
import os
import platform
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "benchmark" / "tasks.jsonl"


def slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-.") or "model"


def get_json(url: str):
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Exact model name known to Ollama")
    parser.add_argument("--runs", type=int, default=1, help="Repetitions per task (default: 1)")
    parser.add_argument("--host", default=os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434"))
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--seed", type=int, default=17)
    args = parser.parse_args()
    if args.runs < 1:
        parser.error("--runs must be at least 1")

    try:
        tasks = [json.loads(line) for line in TASKS.read_text().splitlines() if line.strip()]
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot load benchmark tasks: {exc}", file=sys.stderr)
        return 2

    output_dir = ROOT / "results"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{slug(args.model)}.jsonl"
    endpoint = args.host.rstrip("/") + "/api/chat"
    host = args.host.rstrip("/")
    version_info = get_json(host + "/api/version")
    tags_info = get_json(host + "/api/tags")
    model_digest = None
    if tags_info:
        model_digest = next(
            (item.get("digest") for item in tags_info.get("models", []) if item.get("name") == args.model),
            None,
        )
    runtime_metadata = {
        "ollama_version": version_info.get("version") if version_info else None,
        "model_digest": model_digest,
        "platform": platform.platform(),
        "machine": platform.machine(),
    }
    count = 0
    with output_path.open("a", encoding="utf-8") as out:
        for task in tasks:
            for run in range(1, args.runs + 1):
                body = {
                    "model": args.model,
                    "stream": False,
                    "messages": [{"role": "user", "content": task["prompt"]}],
                    "options": {"temperature": args.temperature, "seed": args.seed + run - 1},
                }
                request = urllib.request.Request(
                    endpoint,
                    data=json.dumps(body).encode("utf-8"),
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                started = time.monotonic()
                record = {
                    "task_id": task["id"],
                    "task_version": task["version"],
                    "category": task["category"],
                    "safety": task["safety"],
                    "run": run,
                    "model_requested": args.model,
                    "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                    "temperature": args.temperature,
                    "seed": args.seed + run - 1,
                    **runtime_metadata,
                    "prompt": task["prompt"],
                }
                try:
                    with urllib.request.urlopen(request, timeout=600) as response:
                        payload = json.load(response)
                    record.update(
                        {
                            "model_returned": payload.get("model"),
                            "response": payload.get("message", {}).get("content", ""),
                            "elapsed_seconds": round(time.monotonic() - started, 3),
                            "prompt_eval_count": payload.get("prompt_eval_count"),
                            "eval_count": payload.get("eval_count"),
                            "done_reason": payload.get("done_reason"),
                        }
                    )
                    print(f"{task['id']} run {run}: captured")
                except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                    record.update({"error": str(exc), "elapsed_seconds": round(time.monotonic() - started, 3)})
                    print(f"{task['id']} run {run}: ERROR {exc}", file=sys.stderr)
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
                out.flush()
                count += 1
    print(f"Wrote {count} records to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
