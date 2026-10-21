# FYP Decisions Log

Final Year Project, Software Design, TUS Athlone. Student: Yu Lin Wan (Steven). Supervisor: Dr Muhammad Naveed Abbas.

**How to use this file:** add a new dated entry whenever a decision is made or changed. Never delete old entries; mark them *Superseded* and link to the new one. Check this file before suggesting changes to anything marked *Settled*.

## Project in one paragraph

Evaluating Prompt Rewriting Strategies for Reliable LLM-Generated Code: A Prototype-Based Approach. Two equal parts: (A) a prototype web app that rewrites coding prompts using three strategies, built with Agile practice; (B) a controlled experiment measuring whether each strategy beats the original prompt on code correctness and consistency.

## People and roles

- **Supervisor:** Dr Muhammad Naveed Abbas. Works professionally in AI, so expect technical questions on method and statistics. Gave written feedback on 2026-10-18.
- **Lecturer (a different person from the supervisor):** raised the scope concerns on 2026-10-15 (topic too broad, "enhancing" ambiguous).

## Settled decisions

### D1. Topic direction: LLM / prompt rewriting (2026-10-12)
- **Decision:** do the FYP on AI/LLM prompt rewriting, not a Unity/XR project.
- **Why:** a web app with LLM API integration, evaluation and measurable results is strong evidence for a software engineering CV. Supervisor later confirmed the idea is suitable (2026-10-18).
- **Status:** Settled.

### D2. Narrow the scope: define "enhanced" as measurable (2026-10-15)
- **Trigger:** lecturer said the topic was too broad and "enhancing" was ambiguous.
- **Decision:** "enhanced" means the generated code **passes more unit tests** and **passes them more consistently across repeated runs**. Not "looks better".
- **Dropped:** multi-domain claims, the user study, Unity focus, LLM-as-judge scoring.
- **Status:** Settled.

### D3. Non-determinism is measured, not eliminated (2026-10-15, refined 2026-10-20)
- **Decision:** treat run-to-run variation as a result. Run each prompt 10 times and report variation.
- **Refinement (2026-10-20):** a fixed seed at temperature 0 would make runs near-identical and the consistency metric meaningless. So: **fixed non-zero temperature (e.g. 0.2), seeds 1-10, identical across all conditions**, plus a **temperature-0 control run** to measure residual non-determinism.
- **Status:** Settled. The exact temperature value is to be confirmed in the pilot.

### D4. Benchmark: about 40 tasks from HumanEval/MBPP, Python only (2026-10-15)
- **Why:** objective unit tests, established pass@k metric, replicable. Unity code is too hard to auto-test.
- **Known risk:** the benchmark may be in the model's training data (contamination). Mitigation: pilot early, use harder or lightly rephrased tasks, state it as a limitation.
- **Status:** Settled.

### D5. Model: small open model run locally via Ollama (2026-10-15)
- **Candidate:** Qwen2.5-Coder 3B (fallback: 1.5B, or a hosted API with a capped budget).
- **Why:** control, no API cost, repeatable. Laptop has an RTX 3050 laptop GPU, so a 7B model is likely too slow.
- **Optional:** one hosted-model check on a subset, to see if results transfer.
- **Status:** Decided but **not yet tested on the laptop** (see open items).

### D6. Three rewriting strategies, deterministic and template-based (2026-10-20)
- **Strategies:** (1) role and context, (2) few-shot examples, (3) structured specification.
- **Decision:** each is a deterministic template, so the same input always gives the same rewrite. Rewrites may only restructure the original information, never add hints or answers. Few-shot examples come from tasks outside the test set.
- **Status:** Settled.

### D7. Statistics (2026-10-20)
- **Decision:** paired Wilcoxon signed-rank test on per-task pass rates; bootstrap 95% confidence intervals; Holm correction across the three comparisons.
- **Status:** Settled.

### D8. Metric definitions (2026-10-20, per supervisor feedback point 4)
- **Correctness:** per task, pass rate = runs passing all unit tests / 10. Per condition, the mean over about 40 tasks. Higher is better.
- **Consistency:** share of tasks whose 10 runs all have the same outcome (all pass or all fail). Secondary: mean per-task standard deviation of pass/fail.
- **Caveat:** always read consistency together with correctness, since a task that always fails is consistent but useless.
- **Status:** Settled.

### D9. Prototype is a core deliverable, built with Agile practice (2026-10-18 feedback, applied 2026-10-20)
- **Trigger:** supervisor said the project looked too research-oriented and asked for stronger software design, implementation and Agile practice.
- **Decision:**
  - Two-week sprints; user stories and backlog on a GitHub Projects board.
  - One branch per story, merged by pull request.
  - GitHub Actions CI running pytest (back end and rewriting module) and Vitest (React).
  - Sprint reviews at supervisor meetings; short retrospective in the repo after each sprint.
  - Definition of Done: merged via pull request, tests passing in CI, acceptance criteria shown at the sprint review.
- **Status:** Settled.

### D10. Architecture and tech stack (2026-10-20)
- React front end -> FastAPI back end (REST/JSON) -> rewriting module (pure Python) -> LLM client (local Ollama API).
- The evaluation harness **reuses the same rewriting module and LLM client**, runs generated code against pytest tests in a Docker sandbox, and writes CSV results. The results page reads that CSV.
- Tooling: Python, pytest, Docker, Ollama, SciPy/statsmodels, pandas, React, FastAPI, Vitest, Git/GitHub.
- **Status:** Settled.

### D11. Initial product backlog (2026-10-20)
- **US1 (Must):** enter a prompt, choose a strategy, get the rewrite (median response time <= 500 ms).
- **US2 (Must):** original and rewrite side by side with a note on what changed.
- **US3 (Must):** send either prompt to the local LLM and see the generated code (<= 60 s).
- **US4 (Should):** results page showing pass rate, consistency and confidence intervals per strategy.
- **US5 (Could):** copy or export the rewritten prompt.
- **Status:** Settled. May be re-prioritised at sprint reviews.

### D12. Prototype evaluation criteria (2026-10-20, per supervisor feedback point 5)
- All Must stories meet their acceptance criteria.
- 100% of unit tests pass in CI; at least 80% line coverage on the rewriting module.
- Median rewrite latency <= 500 ms; generation <= 60 s on the local model.
- 100% of the 120 rewrites (40 prompts x 3 strategies) keep the full original task text and contain every required section (automated check).
- **Status:** Settled. Targets may be adjusted after the pilot measures real speed.

### D13. Out of scope (2026-10-15, expanded 2026-10-20)
Model training or fine-tuning; Unity or game-engine code; other languages or domains; user accounts and deployment; user studies; commercial use.

### D14. Title (2026-10-20, per supervisor feedback point 1)
"Evaluating Prompt Rewriting Strategies for Reliable LLM-Generated Code: A Prototype-Based Approach"
- **Supersedes:** earlier title "Does Prompt Rewriting Improve LLM-Generated Code? Measuring Correctness and Consistency, with a Prototype Tool".

## Timeline (assumed 24 weeks; adjust to the real FYP calendar)

| Weeks | Activity |
|---|---|
| 1-3 | Literature review, metrics, backlog, proposal approval, repo and CI set up |
| 3-7 | Sprints 1-2: rewriting module and LLM client |
| 6-10 | Sprints 3-4: evaluation harness and pilot; design frozen by week 10 |
| 10-14 | Full experiments (about 1,600 generations) |
| 9-15 | Sprints 5-6: FastAPI back end and React front end |
| 14-19 | Sprints 7-8: statistical analysis and results page |
| 18-21 | Sprint 9: prototype evaluation and hardening |
| 20-24 | Final report, demo video, public repository |

## Open items

- [ ] Test the local model on the laptop (install Ollama, run the 3B model, record tokens per second, check GPU use). Choose the final model size based on the result.
- [ ] Confirm the temperature value (e.g. 0.2) after the pilot.
- [ ] Verify every reference (title, authors, year, arXiv number) before submission. They were written from memory.
- [ ] Ask the supervisor whether the 4-page proposal is acceptable (template suggests 1-2 pages).
- [ ] Update the submission date on the proposal if this is a resubmission.
- [ ] Confirm the real FYP calendar and adjust the 24-week plan.
- [ ] Pilot on about 10 tasks to check for a benchmark ceiling effect (contamination).

## Change history of the proposal document

| Version | Date | What changed |
|---|---|---|
| v1 | 2026-10-12 | First draft: general "prompt enhancer" tool plus evaluation |
| v2 | 2026-10-15 | Narrowed to a measurable research question (after lecturer feedback) |
| v3 | 2026-10-20 | Prototype as core deliverable, Agile method, user stories, metric and prototype-evaluation tables (after supervisor feedback) |
