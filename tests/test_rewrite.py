import pytest

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