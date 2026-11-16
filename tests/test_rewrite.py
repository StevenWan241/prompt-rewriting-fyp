from rewriting.rewriter import rewrite

PROMPT = "Write a function add(a, b) that returns the sum of a and b."


def test_role_context_keeps_original_prompt():
    result = rewrite(PROMPT, "role_context")
    assert PROMPT in result