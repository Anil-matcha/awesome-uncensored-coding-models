# Manual coding-agent scenarios

The API runner evaluates one model response per task. Use these scenarios to check whether an agent can call tools and finish a task with the same Muapi model. Run each app in a disposable directory or throwaway repository with no secrets and no valuable files.

## Shared task

Create a small Python package named `stringkit` with a `slugify(text: str) -> str` function. It should lowercase text, replace each run of non-alphanumeric characters with one hyphen, trim leading/trailing hyphens, and handle empty input. Add at least five unit tests. Do not install dependencies or modify files outside this project. Run the tests and summarize the files changed.

This is a benign multi-file edit task: it exercises reading files, planning, writing code, using the terminal, and correcting failures. Keep the starting directory identical for each run.

## Run matrix

For every tested model ID, run the same task once in Codex CLI, Claude Code, and OpenCode. Repeat the task at least three times before drawing conclusions. Record:

- Exact Muapi model ID and its live `capabilities.tools` value.
- App name and version, date, and configured protocol endpoint.
- Whether the agent read files, wrote the implementation/tests, ran tests, and fixed any failures.
- Whether it followed the no-dependencies and directory constraints.
- Final test output, elapsed time, and credits/token usage where available.
- Any manual intervention, unsupported tool call, error, or incomplete step.

Do not treat a model-only API response as proof that an agent can use tools. Keep manual app outcomes separate from the JSONL results produced by `scripts/run_benchmark.py`.

## Results template

| Model ID | App / version | Run | Tests pass | Tool use complete | Constraints followed | Time | Usage | Notes |
|---|---|---:|---|---|---|---:|---|---|

No app/model runs are recorded here yet. The model runner and setup instructions do not imply that every model works equally well in every agent.
