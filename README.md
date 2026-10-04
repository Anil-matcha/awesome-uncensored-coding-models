# Uncensored Coding Models

A reproducible, task based comparison of coding models hosted by Muapi. It also explains how to use eligible models from **Codex CLI, Claude Code, and OpenCode**. The benchmark tracks coding usefulness and refusal behavior separately. “Uncensored” is a community label, not a standardized model property or a guarantee.

## Related projects

- [Awesome Uncensored LLMs](https://github.com/Anil-matcha/awesome-uncensored-llms) — broader model catalog and provenance notes.
- [Awesome Abliterated LLMs](https://github.com/Anil-matcha/awesome-abliterated-llms) — hosted endpoint guide with API examples.
- [Awesome Uncensored AI Agents](https://github.com/Anil-matcha/awesome-uncensored-ai-agents) — general-purpose agent setup and safety guidance.
- [Muapi Abliterated LLM API](https://muapi.ai/abliterated-llm-api) — hosted text models and current tool-capability information.
- [Muapi coding-agent installation guide](https://muapi.ai/docs/ai-agent-install-chat-agents) — configure Codex CLI and Claude Code.
- [Muapi OpenAI-compatible API guide](https://muapi.ai/docs/openai-compatible) — Chat Completions endpoint used by OpenCode and this benchmark runner.
- [Muapi dashboard](https://muapi.ai/dashboard) — create API keys and review usage.
- [Muapi](https://muapi.ai) — hosted model APIs and coding-agent integrations.

## Current status

The Muapi API runner, task set, and agent setup guides are ready. **No model has been scored yet.** Rankings stay empty until runs and review notes are published.

## What this measures

- Coding quality from the same prompts sent to selected Muapi text models.
- Whether models follow task constraints and explain changes clearly.
- Refusal behavior on benign tasks and handling of a non-operational safety control.
- Response time and token usage returned by the API.

This small, human reviewed model benchmark is not a substitute for SWE-bench or a general capability evaluation. The API runner measures one model response at a time; it does not measure how Codex, Claude Code, or OpenCode execute tools across a repository. Use [`agent-scenarios.md`](agent-scenarios.md) for manual, sandboxed app checks. A single run is anecdotal; use at least three runs per task before making stability claims.

## Run the benchmark

Requires Python 3.10+ and a Muapi API key with available credits. No Python packages are required. Each task/run sends a billable hosted API request.

```bash
export MUAPI_API_KEY="your-muapi-api-key"
python3 scripts/run_benchmark.py --model qwen-3-8-27b-obliterated --runs 1
```

The runner reads `GET /v1/models?type=text`, checks the requested ID and tool capability, then sends prompts to `POST /v1/chat/completions`. By default it requires `capabilities.tools: true` because the project focuses on coding-agent models. It writes one JSONL record per task/run to `results/<model-slug>.jsonl`, including the prompt, response, model ID/capabilities, timestamp, elapsed time, settings, and token usage. Results can contain generated code; review them before sharing.

Use `--allow-no-tools` only for a text-only comparison; those models are not eligible for the agent compatibility track. `MUAPI_BASE_URL` can select another trusted Muapi environment. Check current model prices and your balance before running batches; the runner does not estimate cost.

## Use models in coding agents

| App | Muapi endpoint | Protocol | Guide |
|---|---|---|---|
| Codex CLI | `https://api.muapi.ai/openai/v1` | OpenAI Responses | [Setup](integrations.md#codex-cli) |
| Claude Code | `https://api.muapi.ai/anthropic` | Anthropic Messages | [Setup](integrations.md#claude-code) |
| OpenCode | `https://api.muapi.ai/v1` | OpenAI Chat Completions | [Setup](integrations.md#opencode) |

Muapi exposes tool-capable text models through each of these protocols. Verify that the exact model ID appears in the model list for the endpoint your app uses. For agent use, select IDs with `capabilities.tools: true`; availability and capabilities can change. Coding quality varies by model. Multi-turn agent requests can use more credits because the conversation history is sent on each turn. Codex and Claude Code have protocol-specific feature limits; see the setup guide.

## Benchmark tasks and scoring

[`benchmark/tasks.jsonl`](benchmark/tasks.jsonl) covers bug fixes, small feature work, tests, refactoring, documentation, and defensive input handling. Its safety control asks only for classification and a lawful alternative; it does not ask for code or operational steps.

Use [`SCORING.md`](SCORING.md) to rate task completion, code quality, instruction following, and refusal behavior independently. Keep API model results distinct from manual app/tool-use results.

| Model ID | Tools | Runs | Coding score | Benign refusal rate | Safety control | Results |
|---|---:|---:|---:|---:|---|---|
| _No runs recorded yet_ | | | | | | |

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Submit raw records, exact model IDs, task versions, settings, and scoring rationale. Do not invent or infer a model's underlying weights from a hosted alias.

## License

Benchmark tasks, runner, and documentation are licensed under MIT. See [`LICENSE`](LICENSE). Model services and linked third-party tools retain their own terms.
