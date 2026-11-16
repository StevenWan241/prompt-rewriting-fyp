import pytest

from rewriting.rewriter import rewrite

PROMPT = "Write a function add(a, b) that returns the sum of a and b."


def test_role_context_keeps_original_prompt():
    result = rewrite(PROMPT, "role_context")
    assert PROMPT in result

def test_unknown_strategy_raises_value_error():
    with pytest.raises(ValueError):
        rewrite(PROMPT, "FAKETEST")