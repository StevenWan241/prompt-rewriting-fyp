"""Deterministic prompt rewriting strategies (decision D6)."""

ROLE_CONTEXT_TEMPLATE = (
    "You are an expert Python programmer. "
    "Complete the task below and reply with Python code only.\n\n"
    "Task:\n{prompt}\n"
)

STRUCTURED_SPEC_TEMPLATE = (
    "## Task\n"
    "{prompt}\n\n"
    "## Requirements\n"
    "Write correct, working Python code.\n\n"
    "## Output\n"
    "Return Python code only.\n"
)

def rewrite(prompt, strategy):
    """Return the prompt rewritten with the chosen strategy."""
    if strategy == "role_context":
        return ROLE_CONTEXT_TEMPLATE.format(prompt=prompt)
    elif strategy == "structured_spec":
        return STRUCTURED_SPEC_TEMPLATE.format(prompt=prompt)
    raise ValueError(f"Unknown strategy: {strategy}")