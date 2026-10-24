# Refusal test (Oct 2026): raw outputs

Raw answers and scores behind the video "Best Uncensored Coding Models (Tested)".

- Prompts: 7 of the 10 benign "Malware/Hacking" prompts from JBB-Behaviors (MIT), `jbb_malware_hacking_10.jsonl`. jbb-0, 1, 2, 4, 6, 7, 9 were scored.
- Models: `mimo-v2-6-flash-abliterated` (uncensored, hosted) vs two mainstream models, 3 runs per prompt.
- Result (refused runs out of 21): uncensored 0, mainstream A 16, mainstream B 7. See `SCORES.md` for per-run labels and hand-read notes.
- Scope: refusals only, one uncensored model, seven prompts. "Answered" is a label, not a claim that the answer was good or safe. Code quality was not scored, and it is not a full ranking.
- Files: `bench_*.jsonl` are every raw response; `scores.json` is the machine-readable score table.
