# Pilot tasks

Drawn on 2026-11-16 by `scripts/draw_pilot_tasks.py`, following decision D18.

## Method
- Seeded random sample, seed 42, using Python's `random.Random`.
- Pool: HumanEval (164 tasks, `test` split) and MBPP sanitized `test` split (257 tasks).
- The MBPP `prompt` split (7 tasks) is kept out of the pool for few-shot examples (D6).
- Ids are sorted before sampling, so the draw does not depend on row order.
- 5 tasks from each set, 10 in total.
- Exclusions: none. Every task in the pool has unit tests.

## Pilot tasks
- HumanEval: 99, 123, 103, 161, 154
- MBPP: 113, 61, 274, 257, 245

## Rules for these tasks
- The pilot uses the original prompts only. It is a feasibility check, not a result.
- Do not tune rewrite templates on these tasks. Either drop them from the final 40 or log them as tuning tasks.

## Reproduce
Run `pip install datasets`, then `python scripts/draw_pilot_tasks.py`. The output is identical every time.