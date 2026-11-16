import pytest
import statistics
import time

from rewriting.rewriter import rewrite

PROMPT = "Write a function add(a, b) that returns the sum of a and b."

STRATEGIES = ["role_context", "few_shot", "structured_spec"]

@pytest.mark.parametrize("strategy", STRATEGIES)
def test_rewrite_keeps_original_prompt(strategy):
    result = rewrite(PROMPT, strategy)
    assert PROMPT in result

def test_unknown_strategy_raises_value_error():
    with pytest.raises(ValueError):
        rewrite(PROMPT, "FAKETEST")

@pytest.mark.parametrize("strategy", STRATEGIES)
def test_median_rewrite_time_is_under_500_ms(strategy):
    times_ms = []
    for _ in range(100):
        start = time.perf_counter()
        rewrite(PROMPT, strategy)
        times_ms.append((time.perf_counter() - start) * 1000)
    assert statistics.median(times_ms) <= 500