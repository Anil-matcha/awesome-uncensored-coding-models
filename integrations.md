# Use Muapi models in coding agents

Create a Muapi key in the [dashboard](https://muapi.ai/dashboard), then export it as `MUAPI_API_KEY`. Keep keys in your environment or the app's credential store; do not commit them. List current text model IDs and capabilities before choosing a model:

```bash
curl -s "https://api.muapi.ai/v1/models?type=text" \
  -H "Authorization: Bearer $MUAPI_API_KEY"
```

For file edits and terminal tools, choose a model with `capabilities.tools: true`. Model IDs and capabilities can change; use the live response rather than copying an old list. Codex and Claude Code expose protocol-specific model lists; verify the model ID against the app's endpoint too.

## Codex CLI

Muapi's Codex-compatible endpoint uses the OpenAI Responses protocol. Add this to `~/.codex/config.toml`:

```toml
model = "qwen-3-8-27b-obliterated"
model_provider = "muapi"

[model_providers.muapi]
name = "Muapi"
base_url = "https://api.muapi.ai/openai/v1"
env_key = "MUAPI_API_KEY"
wire_api = "responses"
```

Export the key and start Codex:

```bash
export MUAPI_API_KEY="your-muapi-api-key"
codex
```

Use an exact model ID listed by `GET https://api.muapi.ai/openai/v1/models`. Tool-capable community model variants work through Muapi's Responses-to-chat translation. Check Codex tool limitations and output/context limits in [Muapi's Codex guide](https://muapi.ai/docs/ai-agent-codex-cli).

## Claude Code

Claude Code uses Muapi's Anthropic Messages endpoint. In a shell where Claude Code will run:

```bash
export MUAPI_API_KEY="your-muapi-api-key"
export ANTHROPIC_BASE_URL="https://api.muapi.ai/anthropic"
export ANTHROPIC_AUTH_TOKEN="$MUAPI_API_KEY"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen-3-8-27b-obliterated"
export ANTHROPIC_SMALL_FAST_MODEL="qwen-3-8-27b-obliterated"
claude --model qwen-3-8-27b-obliterated
```

Use a tools-capable model ID from `GET https://api.muapi.ai/anthropic/v1/models`. The two background-model variables need to point at a valid model too. See [Muapi's Claude Code guide](https://muapi.ai/docs/ai-agent-claude-code) for behavior, billing, and troubleshooting notes.

## OpenCode

OpenCode uses Muapi's OpenAI Chat Completions endpoint. Set the key in the shell that starts OpenCode:

```bash
export MUAPI_API_KEY="your-muapi-api-key"
```

Add a provider to `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "muapi": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Muapi",
      "options": {
        "baseURL": "https://api.muapi.ai/v1",
        "apiKey": "{env:MUAPI_API_KEY}"
      },
      "models": {
        "qwen-3-8-27b-obliterated": {
          "name": "Qwen 3.8 27B Obliterated"
        }
      }
    }
  }
}
```

Replace the example ID with a live text model ID whose capabilities include `tools: true`. In OpenCode, run `/models` and select it under Muapi. See [Muapi's OpenCode guide](https://muapi.ai/docs/opencode) and [OpenCode's provider documentation](https://opencode.ai/docs/providers/).

## Shared cautions

- Agent use requires tool-calling support. The benchmark runner checks the live model list and requires it by default.
- “Uncensored” does not describe a standardized capability or guarantee. Evaluate the exact model ID and your specific workload.
- Agent turns can resend the full conversation, so long sessions may use credits quickly. Check the current model price and balance first.
- Smaller models may miss steps on multi-file work. Review diffs and run the project's own checks in a disposable working copy.
- Do not put API keys in committed project config, prompts, screenshots, or benchmark result files.
