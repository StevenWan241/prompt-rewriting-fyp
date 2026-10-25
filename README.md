# prompt-rewriting-fyp

Final year project (Software Design, TUS Athlone): evaluating prompt-rewriting
strategies for reliable LLM-generated code, with a prototype web tool.

## What this project does

- **Experiment:** tests whether three rewriting strategies (role and context,
  few-shot, structured specification) beat the original prompt on code
  correctness (unit-test pass rate) and consistency (variation across 10
  repeated runs). About 40 HumanEval/MBPP tasks, Python only.
- **Prototype:** a web tool that rewrites a coding prompt with a chosen
  strategy, shows original and rewrite side by side, and sends either to a
  local model.

Both parts share the same rewriting module and LLM client.

## Repository layout

| Folder | Contents |
| --- | --- |
| `rewriting/` | Rewriting module (three deterministic, template-based strategies) |
| `backend/` | FastAPI back end and LLM client |
| `frontend/` | React front end |
| `harness/` | Experiment harness: runs generated code against tests in a Docker sandbox, writes CSV results |
| `docs/` | Evidence and write-ups, e.g. `ollama-speed-test.md` |

Design decisions are recorded in `decisions-log.md`.

## Status

Early setup (October 2026). Not yet runnable.

## Model and licence notes

- Local model: Qwen2.5-Coder 3B, run through Ollama. It is licensed under the
  Qwen Research License (non-commercial research or evaluation use only).
  Model weights are not included in this repository; install with
  `ollama pull qwen2.5-coder:3b`.
- Benchmark tasks come from HumanEval and MBPP. Check each dataset's licence
  before copying any data into this repository.
- This project's own code is under the licence in `LICENSE` (MIT).

## Requirements

Python, Docker, Ollama, Node.js. Setup instructions will be added as the
prototype develops.
