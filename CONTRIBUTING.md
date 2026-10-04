# Contributing

## Add a model result

1. Follow the run instructions in `README.md` and run the same task file used for the other models.
2. Include raw JSONL records. Do not edit model responses after capture.
3. Record exact model identifier and digest, quantization, runtime version, hardware, date, and generation options.
4. Score each task using `SCORING.md`, with a brief rationale. Keep coding scores separate from refusal labels.
5. Identify unavailable models, failed runs, and deviations; do not silently substitute a model.

## Add or revise a task

Tasks must be self-contained, benign, and answerable without external services or private data. Keep one task per JSONL line with a stable ID. Describe objective acceptance criteria in the task text. Do not add malware, exploit deployment, credential theft, stealth, or evasion requests. If a task changes materially, increment its version and do not mix its results with the earlier version.

## Claims and sources

Link primary model cards and runtime documentation. “Uncensored” is an informal community label, not a guarantee. Distinguish open weights from hosted services and record the specific artifact tested. Do not claim a model is safe, private, or unrestricted without evidence for the exact configuration.
