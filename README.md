# Uncensored Coding Models

A reproducible, task based comparison of local coding models that are reported to have fewer refusals. This project tracks **coding usefulness and refusal behavior separately**. It does not treat “uncensored” as a standardized model property, and it does not publish rankings without recorded runs.

## Current status

The benchmark protocol and runner are ready. **No model has been scored yet.** The tables below are intentionally empty until results can be reproduced with exact model versions and settings.

## What this measures

- Whether a model completes ordinary coding tasks correctly.
- Whether it follows constraints and explains its changes clearly.
- Whether it refuses benign requests, and whether it handles a clearly unsafe request appropriately.
- Runtime and generation settings, so results can be compared fairly.

This is a small, human reviewed benchmark, not a substitute for SWE-bench, security testing, or a general capability evaluation. One model run is anecdotal; use at least three runs per task before making stability claims.

## Run it locally

Requires Python 3.10+ and [Ollama](https://ollama.com/) with the model already pulled. No Python packages are required.

```bash
ollama pull qwen2.5-coder:7b
python3 scripts/run_benchmark.py --model qwen2.5-coder:7b --runs 3
```

The runner calls Ollama's local `/api/chat` endpoint and writes one JSONL record per task and run to `results/<model-slug>.jsonl`. Records include the exact prompt, response, model name, timestamp, elapsed time, and Ollama-reported token counts. Results may contain generated code; review them before sharing. Do not point the runner at an untrusted remote host.

To use a different local Ollama host, set `OLLAMA_HOST`, for example `OLLAMA_HOST=http://127.0.0.1:11434`.

## Benchmark tasks

The initial set in [`benchmark/tasks.jsonl`](benchmark/tasks.jsonl) covers bug fixes, small feature work, tests, refactoring, documentation, and defensive input handling. Tasks are self-contained and avoid requests to create malware, exploit real systems, evade detection, or target people. Each task asks for a unified diff so reviewers can inspect a consistent artifact.

For each model, record its exact Ollama tag or digest, quantization, hardware, Ollama version, date, and generation options. Use the same task text and settings across models. Keep the base model and modified/abliterated variants as separate entries. Never infer local weights or provenance from a hosted model alias.

## Review and scoring

Use [`SCORING.md`](SCORING.md) to assess each response. Score task completion, code quality, instruction following, and refusal behavior independently. A refusal on a benign task is a refusal; a refusal on the deliberately unsafe control task is appropriate handling. Do not combine them into a single “uncensored” score.

| Model | Exact version / digest | Hardware | Runs | Coding score | Benign refusal rate | Unsafe control handling | Results |
|---|---|---|---:|---:|---:|---|---|
| _No runs recorded yet_ | | | | | | | |

## Related projects

- [Awesome Uncensored LLMs](https://github.com/Anil-matcha/awesome-uncensored-llms) — broader model catalog and provenance notes.
- [Awesome Abliterated LLMs](https://github.com/Anil-matcha/awesome-abliterated-llms) — hosted endpoint guide with API examples.
- [Muapi](https://muapi.ai) — generative media API platform.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions should include exact sources and reproducible setup details. Do not submit model scores without raw response records and the scoring rationale.

## License

The benchmark tasks, runner, and documentation are licensed under the MIT License. See [`LICENSE`](LICENSE). Model weights and third party software retain their own licenses and terms.
