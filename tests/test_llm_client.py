from llm.client import build_payload

def test_payload_has_model_prompt_and_no_streaming():
    payload = build_payload("write add(a, b)", seed=3)
    assert payload["model"] == "qwen2.5-coder:3b"       # the tag from ollama list
    assert payload["prompt"] == "write add(a, b)"
    assert payload["stream"] is False      # we want one full reply, not chunks

def test_payload_sets_temperature_and_seed():
    payload = build_payload("write add(a, b)", seed=3)
    assert payload["options"]["temperature"] == 0.2   # your D3 value
    assert payload["options"]["seed"] == 3