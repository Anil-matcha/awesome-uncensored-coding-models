# Awesome Uncensored Coding Models

A curated directory of language models people use or evaluate for programming, software maintenance, and coding-agent work. It focuses on models described by their communities as **uncensored**, **abliterated**, **derestricted**, or **low-refusal**. This project records exact model IDs, access methods, coding use cases, and evidence where available.

“Uncensored” is an informal label, not a standardized model property or promise. It does not mean a model is unrestricted, accurate, secure, private, or suitable for every use. Evaluate the exact model and host for your task, and follow the applicable terms and acceptable-use rules.

## Contents

- [Coding use cases](#coding-use-cases)
- [Hosted coding candidates](#hosted-coding-candidates)
- [Choosing a model for a workflow](#choosing-a-model-for-a-workflow)
- [Use with coding agents](#use-with-coding-agents)
- [Evaluation and results](#evaluation-and-results)
- [Run the benchmark](#run-the-benchmark)
- [Contribute a model or result](#contribute-a-model-or-result)

## Coding use cases

Low-refusal or abliterated models can be evaluated for the same ordinary software work as other LLMs. This list is useful when you want to compare how a model handles a task, integrate it into an agent, or test a hosted endpoint before adopting it.

| Use case | What to try | What to check |
|---|---|---|
| **Generate a small feature** | Give the model a precise function or endpoint requirement and acceptance criteria. | Correctness, edge cases, dependencies added, and whether it follows the requested format. |
| **Debug an existing implementation** | Provide a minimal failing example, expected behavior, and observed behavior. | Whether the proposed fix addresses the cause and preserves existing behavior. |
| **Write or improve tests** | Ask for tests against a documented contract, including boundary and invalid-input cases. | Whether tests are meaningful, independent, and fail for the right reason. |
| **Refactor code** | State behavior that must remain unchanged and ask for a focused diff. | Regressions, unnecessary changes, readability, and instruction following. |
| **Explain unfamiliar code** | Share a small module or function and ask for a concise explanation or call flow. | Factual grounding in the supplied code; ask it to identify uncertainty instead of guessing. |
| **Review a patch** | Supply a diff and ask for prioritized, actionable findings. | False positives, missed edge cases, and whether each finding points to concrete code. |
| **Work across a repository** | Connect a tool-capable model to a coding agent and ask it to inspect, edit, and verify a small task. | File selection, tool-call reliability, test execution, constraint following, and the final diff. |
| **Understand screenshots or diagrams** | Use a model that advertises vision with a coding-agent workflow that accepts image input. | Whether the chosen endpoint and agent actually pass image inputs through. Vision metadata alone does not prove end-to-end image support. |

Start with a small, reversible task. For repository work, use a disposable checkout or branch, inspect every change, and run the project’s own checks before merging. Do not send secrets, customer data, or proprietary source code to a hosted service unless you have approval to do so.

## Hosted coding candidates

The following Muapi-hosted model IDs currently advertise tool calling, which makes them candidates for agent workflows. The shortlist is **not ranked** and does not claim measured coding ability. `Thinking` and `Vision` reflect the host’s capability metadata, not independent testing.

| Hosted model ID | Tools | Thinking | Vision | Good first evaluation |
|---|---:|---:|---:|---|
| `qwen-3-8-27b-abliterated` | Yes | Yes | Yes | Compare on multi-step bug fixes, test generation, and image-assisted tasks. |
| `qwen-3-8-27b-obliterated` | Yes | Yes | Yes | Compare alongside the abliterated variant on the same prompts. |
| `glm-5-3-abliterated` | Yes | No | No | Try on feature implementation, code review, and repository tool use. |
| `gemma-4-31b-gembrain-abliterated` | Yes | No | Yes | Try on coding tasks and image-input workflows where supported end to end. |
| `mimo-v2-6-flash-abliterated` | Yes | No | Yes | Include in general coding and tool-call reliability comparisons. |
| `abliterated-model-large-v2` | Yes | No | No | Treat as a hosted alias; do not infer its underlying model from the name. |
| `glm-5-3-flash-abliterated` | Yes | No | Yes | Compare with the non-flash GLM variant on identical tasks. |
| `gemma-4-26b-a4b-abliterated` | Yes | No | No | Compare with the 31B Gemma variant using the same task set. |
| `qwen-3-5-27b-opus-distilled-derestricted` | Yes | No | Yes | Compare on instruction following and agent-tool workflows. |

“Good first evaluation” describes a test to run, not a claim that the model performs well at it. The repository has not scored these models yet.

### Model references and lineage

These primary sources describe related upstream families or base models, not necessarily the exact hosted fine-tune behind a Muapi ID. The host alias does not by itself verify checkpoint identity, training recipe, license, or downloadable-weight availability.

- [Qwen3.8-27B model card](https://huggingface.co/Qwen/Qwen3.8-27B) describes coding, long-horizon agentic tasks, image/video input, and official model downloads.
- [GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3) describes coding and agentic software work for the upstream GLM model.
- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4) describes coding, function calling, multimodal input, and open-weight variants in the Gemma 4 family.
- [Xiaomi MiMo-V2-Flash project](https://github.com/XiaomiMiMo/MiMo-V2-Flash) describes coding and agentic capabilities for its upstream model.

For an upstream downloadable model, follow its own model card and license. Do not assume that an abliterated or derestricted hosted variant has the same license, weights, prompt format, or behavior as the upstream model.

**Source and freshness:** IDs and flags were checked against [Muapi’s live text-model list](https://api.muapi.ai/v1/models?type=text) on 2026-10-06. Availability and capabilities can change; query the live endpoint before configuring an agent. These are hosted API IDs. Listing them here does not establish that the underlying weights are open, downloadable, independently verified, or available from another host.

### Muapi access and documentation

- [Abliterated LLM API catalog](https://muapi.ai/abliterated-llm-api)
- [API guide and examples](https://github.com/Anil-matcha/awesome-abliterated-llms)
- [Coding-agent installation guide](https://muapi.ai/docs/ai-agent-install-chat-agents)
- [OpenAI-compatible API guide](https://muapi.ai/docs/openai-compatible)
- [Dashboard and API keys](https://muapi.ai/dashboard)

## Choosing a model for a workflow

There is no evidence-based “best model” ranking in this repository yet. Use capabilities to narrow the candidates, then compare them on your own representative tasks.

1. **Decide whether you need an agent.** For a single code suggestion or explanation, tool calling is not required. For an agent that reads files, edits a project, or runs commands, choose a model and endpoint that advertise and support tool calling.
2. **Check required inputs.** If your task includes screenshots or diagrams, check vision support at the model, API, and coding-agent layers. A `vision: true` flag alone does not confirm that a given integration forwards images correctly.
3. **Choose a task set.** Include examples from your actual work: bug fixes, tests, refactoring, code review, documentation, or multi-file edits. Keep prompts and acceptance criteria fixed when comparing models.
4. **Run more than once.** Model outputs can vary. Repeat tasks, preserve raw responses, and report failures and missing runs rather than silently dropping them.
5. **Review cost and constraints.** Check current pricing, context/output limits, rate limits, retention terms, and service policies with the host. This repository does not assume these details from a model name.

### Quick selection guide

- **Single-turn code generation or explanation:** tool calling is unnecessary. Use a text endpoint and compare correctness against explicit tests.
- **Repository edits with Codex, Claude Code, or OpenCode:** begin with a candidate that advertises tool calling, then verify that it is listed by the exact agent endpoint and can complete the same disposable task repeatedly.
- **Tasks that need deliberate multi-step reasoning:** include candidates marked `Thinking: Yes` in the comparison. This flag is host metadata; it does not establish that reasoning is enabled for every request or that results will be better.
- **Screenshot-to-code or diagram-assisted work:** include a candidate marked `Vision: Yes`, then verify image support through the full provider and agent path before relying on it.
- **Inline autocomplete or fill-in-the-middle (FIM):** this directory does not currently verify FIM support for these hosted chat IDs. Check whether your editor needs a completion-specific model/API before configuring one.
- **Local or air-gapped coding:** use a downloadable checkpoint only when its own model card, license, inference runtime, and hardware needs support that setup. The hosted Muapi aliases listed above are not evidence that their underlying weights are downloadable.

For comparisons in this repository, report task completion, code quality, instruction following, refusal behavior, latency, and token use separately. See [SCORING.md](SCORING.md) for the rubric.

### A repeatable coding task brief

Use a clear task statement so models can be compared fairly. For example:

```text
Inspect the project and fix the bug described below.
Expected behavior: [specific observable behavior]
Current behavior: [failing example or error]
Constraints: [language/runtime, files to avoid, dependencies allowed]
Acceptance checks: [tests or commands that must pass]
Before editing, summarize the likely cause. Make the smallest suitable change,
run the checks, and report files changed plus any remaining uncertainty.
```

For an agent comparison, keep the repository state, permissions, task, tools, and acceptance checks the same for every model. Record whether the agent inspected relevant files, made a focused patch, ran checks, and reported failures accurately.

## Use with coding agents

Tool-capable model IDs can be tried with the following coding agents through Muapi-compatible endpoints. Confirm the exact model appears in the endpoint’s current model list. Protocol support can differ by application; a model being present in one list does not guarantee it works in every agent.

| Agent | Muapi endpoint and protocol | Setup |
|---|---|---|
| Codex CLI | `https://api.muapi.ai/openai/v1` — OpenAI Responses | [Setup](integrations.md#codex-cli) |
| Claude Code | `https://api.muapi.ai/anthropic` — Anthropic Messages | [Setup](integrations.md#claude-code) |
| OpenCode | `https://api.muapi.ai/v1` — OpenAI Chat Completions | [Setup](integrations.md#opencode) |

Before using an agent on a real project:

- Try the shared task in [agent-scenarios.md](agent-scenarios.md) in a throwaway directory.
- Review the plan, tool calls, final diff, and test output yourself.
- Keep API keys in environment variables or the agent’s secret store; never commit them.
- Watch usage: multi-turn requests may resend conversation history and consume additional credits.
- Do not let an experimental model run destructive commands or access production credentials without appropriate controls.

## Evaluation and results

This repository contains a small prompt set and a runner for comparing individual model responses. **No model results have been published yet.** The candidate table is a starting point for evaluation, not a leaderboard or recommendation.

The prompt set in [`benchmark/tasks.jsonl`](benchmark/tasks.jsonl) covers bug fixing, features, test writing, refactoring, SQL, documentation, defensive input handling, data handling, and instruction following. It also includes a safety-control prompt that asks for classification and a lawful alternative, not operational instructions.

The API runner measures one response to one prompt at a time. It does not measure an agent’s ability to inspect a repository, call tools, edit files, and recover from errors. Manual agent results belong in the separate [agent scenarios](agent-scenarios.md), with app version and tool-use details recorded.

For numeric summaries, use the same task versions and settings and at least three runs per task. Keep per-task scores and raw output with any aggregate; report errors, missing runs, model IDs, capability flags, date, settings, token use, and latency. Do not compare incompatible runs as if they were one benchmark. See [SCORING.md](SCORING.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Run the benchmark

The runner requires Python 3.10+, a Muapi API key, and available credits. It uses only the Python standard library. Each task/run makes a billable API call.

```bash
export MUAPI_API_KEY="your-muapi-api-key"
python3 scripts/run_benchmark.py --model qwen-3-8-27b-abliterated --runs 1
```

The runner checks the live Muapi text-model list and, by default, requires `capabilities.tools: true`. It sends prompts to Chat Completions and appends raw records to `results/<model-id>.jsonl`. The output includes the prompt and model response, so review it before sharing. Check current prices and your balance; the runner does not estimate batch cost.

Use `--allow-no-tools` only for text-only comparisons. To select another trusted Muapi environment, set `MUAPI_BASE_URL` to its API root ending in `/v1`. The API key is read from the environment and is not written to results.

## Contribute a model or result

This is a curated directory, so entries should have a clear programming use case and verifiable source information. Contributions may cover hosted APIs or downloadable models; keep those access types distinct.

For each model entry, include:

- Exact model name/ID and a primary model-card or host source.
- Whether access is hosted, downloadable, or both; include the provider where relevant.
- Verified coding focus or use case, without inferring it from model size or branding alone.
- Tool-calling, vision, and other relevant capabilities, with a source and date checked.
- License, access, or availability caveats when known; say “not verified” when they are not.

For benchmark results, include raw records, exact IDs, task versions, settings, run counts, errors, and scoring rationale. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and [SCORING.md](SCORING.md). Do not publish keys, private data, or generated code that contains secrets.

## Related lists

- [Awesome Uncensored LLMs](https://github.com/Anil-matcha/awesome-uncensored-llms) — broader model catalog and provenance notes.
- [Awesome Abliterated LLMs](https://github.com/Anil-matcha/awesome-abliterated-llms) — hosted endpoint guide and API examples.
- [Awesome Uncensored AI Agents](https://github.com/Anil-matcha/awesome-uncensored-ai-agents) — agent setup and safety guidance.

## License

The benchmark tasks, runner, and documentation in this repository are MIT licensed; see [LICENSE](LICENSE). Listed models, APIs, and coding-agent applications retain their own terms.
