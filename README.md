# Awesome Uncensored Coding Models

A curated list of coding-capable LLMs described by their communities as **uncensored**, **abliterated**, **derestricted**, or **low-refusal**. This catalog focuses on models that can help with programming and coding-agent workflows, with hosted Muapi model IDs listed as a currently maintained source.

“Uncensored” is an informal label, not a standardized property or promise. It does not mean a model is unrestricted, accurate, secure, or suitable for every use. Check the exact model, host, terms, and capabilities before use.

## Coding candidates

The candidates below are currently listed by Muapi with tool-calling support, which is useful for coding agents. The shortlist is **not ranked**: this project has not published coding scores for these models. Tool support is a compatibility signal, not proof of coding quality.

| Model ID | Tool calling | Thinking | Notes |
|---|---:|---:|---|
| `qwen-3-8-27b-abliterated` | Yes | Yes | General-purpose coding candidate |
| `qwen-3-8-27b-obliterated` | Yes | Yes | General-purpose coding candidate |
| `glm-5-3-abliterated` | Yes | No | General-purpose coding candidate |
| `gemma-4-31b-gembrain-abliterated` | Yes | No | General-purpose coding candidate |
| `mimo-v2-6-flash-abliterated` | Yes | No | General-purpose coding candidate |
| `abliterated-model-large-v2` | Yes | No | Hosted alias; underlying model details are not inferred here |
| `glm-5-3-flash-abliterated` | Yes | No | Flash variant |
| `gemma-4-26b-a4b-abliterated` | Yes | No | General-purpose coding candidate |
| `qwen-3-5-27b-opus-distilled-derestricted` | Yes | No | Distilled variant |

**Source and freshness:** IDs and capability flags were checked against [Muapi’s live text-model list](https://api.muapi.ai/v1/models?type=text) on 2026-10-06. Availability and flags may change; query the live list before configuring an agent. These are hosted API IDs. Their presence here does not establish that the underlying weights are open, downloadable, or independently verified.

### Browse and use the Muapi catalog

- [Abliterated LLM API catalog](https://muapi.ai/abliterated-llm-api)
- [API guide and examples](https://github.com/Anil-matcha/awesome-abliterated-llms)
- [Coding-agent installation guide](https://muapi.ai/docs/ai-agent-install-chat-agents)
- [OpenAI-compatible API guide](https://muapi.ai/docs/openai-compatible)
- [Dashboard and API keys](https://muapi.ai/dashboard)

## Evaluation status

This repository includes a small, reproducible prompt set and a runner for comparing model responses. **No model results have been published yet**, so the list above is a starting shortlist, not a recommendation or leaderboard. We track task completion, code quality, instruction following, refusal behavior, latency, and token usage separately. Read [SCORING.md](SCORING.md) before interpreting results.

The API runner measures a model’s single response to a prompt. It does not measure an agent’s ability to inspect a repository, call tools, edit files, and recover from errors. Manual coding-agent checks are documented separately in [agent-scenarios.md](agent-scenarios.md).

## Run the Muapi benchmark

The runner requires Python 3.10+, a Muapi API key, and available credits. It uses only the Python standard library; each task/run sends a billable API request.

```bash
export MUAPI_API_KEY="your-muapi-api-key"
python3 scripts/run_benchmark.py --model qwen-3-8-27b-abliterated --runs 1
```

The runner checks that the model ID exists in Muapi’s live text-model list and, by default, that it advertises tool calling. It sends prompts to the Chat Completions endpoint and appends raw records to `results/<model-id>.jsonl`. Results may contain generated code; review them before sharing. Check current prices and balance before running batches.

Use `--allow-no-tools` only for text-only comparisons. To use another trusted Muapi environment, set `MUAPI_BASE_URL` to its API root ending in `/v1`.

For more reliable comparisons, use the same task versions and settings, run each task at least three times, preserve raw outputs, and report failures and missing runs. Do not publish an aggregate score without the per-task results and scoring rationale.

## Coding-agent setup

Tool-capable model IDs can be tried with the coding agents below through Muapi’s compatible endpoints. Confirm the exact ID appears in that endpoint’s live model list; model support and protocol behavior can vary.

| Coding agent | Muapi protocol endpoint | Setup |
|---|---|---|
| Codex CLI | `https://api.muapi.ai/openai/v1` — Responses | [Setup](integrations.md#codex-cli) |
| Claude Code | `https://api.muapi.ai/anthropic` — Messages | [Setup](integrations.md#claude-code) |
| OpenCode | `https://api.muapi.ai/v1` — Chat Completions | [Setup](integrations.md#opencode) |

Agent turns may resend conversation history and use more credits. Review generated changes, keep API keys out of committed files, and try new models in a disposable project first.

## Add a model or result

Contributions can add a coding-capable model from another host, a verified model card, or reproducible benchmark results. Include the exact model and host IDs, source links, access type (hosted API or downloadable weights), tool-calling status, date checked, and any license or availability caveats. Do not infer model provenance from a hosted alias.

For benchmark results, include raw records, task versions, settings, failures, run count, and scoring rationale. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and [SCORING.md](SCORING.md). Never publish API keys or private data.

## Related lists

- [Awesome Uncensored LLMs](https://github.com/Anil-matcha/awesome-uncensored-llms) — broader model catalog and provenance notes.
- [Awesome Abliterated LLMs](https://github.com/Anil-matcha/awesome-abliterated-llms) — hosted endpoint guide and API examples.
- [Awesome Uncensored AI Agents](https://github.com/Anil-matcha/awesome-uncensored-ai-agents) — agent setup and safety guidance.

## License

The benchmark tasks, runner, and documentation in this repository are MIT licensed; see [LICENSE](LICENSE). Listed models, APIs, and coding-agent applications are governed by their respective terms.
