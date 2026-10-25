# Ollama speed test: Qwen2.5-Coder 3B

Feasibility evidence for the technical and time sections of the feasibility study.

## Setup

| Item | Value |
| --- | --- |
| Date | 24 Oct 2026 (about 19:30-19:40 local time) |
| Ollama version | 0.40.11 |
| Model tag | `qwen2.5-coder:3b` (ID `f72c60cabf62`, 1.9 GB download, 2.2 GB loaded) |
| GPU | NVIDIA GeForce RTX 3050 Laptop GPU |
| VRAM | 4096 MiB total, 0 MiB used before the test |
| Driver | NVIDIA-SMI 610.88, CUDA UMD 13.3 |
| Context window | 4096 tokens (Ollama default) |
| Power and apps | Charger plugged in; Games Launcher and game closed |

## Command and prompt

```
ollama run qwen2.5-coder:3b --verbose
```

Same prompt for all three runs, in one interactive chat:

```
Write a Python function that takes a list of integers and returns the second largest unique value, or None if there is none. Include only the code.
```

## Raw results

### Run 1 (first run after loading the model)

```
total duration:       54.7471549s
load duration:        9.3008ms
prompt eval count:    59 token(s)
prompt eval duration: 39.454158s
prompt eval rate:     1.50 tokens/s
eval count:           125 token(s)
eval duration:        15.27755s
eval rate:            8.18 tokens/s
```

### Run 2

```
total duration:       4.9725785s
load duration:        4.0861134s
prompt eval count:    445 token(s)
prompt eval duration: 258.334ms
prompt eval rate:     1722.58 tokens/s
eval count:           44 token(s)
eval duration:        619.121ms
eval rate:            71.07 tokens/s
```

### Run 3

```
total duration:       922.4711ms
load duration:        9.4846ms
prompt eval count:    528 token(s)
prompt eval cached:   488 token(s)
prompt eval duration: 300.36ms
prompt eval rate:     133.17 tokens/s
eval count:           44 token(s)
eval duration:        604.541ms
eval rate:            72.78 tokens/s
```

### `ollama ps` after run 3

```
NAME                ID              SIZE      PROCESSOR    CONTEXT    RUNNER      UNTIL
qwen2.5-coder:3b    f72c60cabf62    2.2 GB    100% GPU     4096       llamacpp    4 minutes from now
```

## Summary

| Measure | Result |
| --- | --- |
| Generation speed (runs 2 and 3) | 71.07 and 72.78 tokens/s, about 72 tokens/s |
| Run 1 generation speed | 8.18 tokens/s (conditions differed: TODO what changed before run 2) |
| Where the model runs | 100% GPU |
| Output length | 125, 44 and 44 tokens (varies between runs) |
| Licence | Qwen Research License: non-commercial research or evaluation use only |

## Notes and limits

- **Run 1 is not representative.** It was about nine times slower than runs 2 and 3. Cause not confirmed; likely warm-up or GPU contention. Repeat from a cold start before relying on the figure.
- **Runs 2 and 3 are not independent.** Interactive `ollama run` keeps the chat history, so prompt eval counts grew (59, 445, 528) and run 3 reused cached prompt tokens. The prompt eval rate in run 3 is not a real prompt speed. The harness must send each generation as a fresh, independent request through the Ollama API.
- **One short prompt only.** The few-shot and structured-specification rewrites are much longer. Measure speed again with those lengths. The 4096-token context is shared by prompt and answer, so check that the longest rewrite plus a typical answer fits.
- **Output format.** The model was asked for code only and still added comments and an explanation in run 1. The harness must extract the code block before running tests.
- **Not yet measured:** Docker sandbox start-up time and test run time per generation, which may cost more than the generation itself.

## Provisional estimate (not a result)

At about 72 tokens/s, an answer of 100-300 tokens takes roughly 1.5-4.5 s, so 1,600 generations would be roughly 0.7-2 hours of generation time. This excludes prompt processing and the sandbox run per generation. Confirm in the pilot before using this number anywhere.
