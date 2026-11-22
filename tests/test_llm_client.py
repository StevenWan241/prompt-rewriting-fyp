from unittest.mock import MagicMock, patch
from llm.client import build_payload, generate

def test_payload_has_model_prompt_and_no_streaming():
    payload = build_payload("write add(a, b)", seed=3)
    assert payload["model"] == "qwen2.5-coder:3b"       # the tag from ollama list
    assert payload["prompt"] == "write add(a, b)"
    assert payload["stream"] is False      # we want one full reply, not chunks

def test_payload_sets_temperature_and_seed():
    payload = build_payload("write add(a, b)", seed=3)
    assert payload["options"]["temperature"] == 0.2   # your D3 value
    assert payload["options"]["seed"] == 3

def test_generate_returns_response_text():
    fake = MagicMock()
    fake.status_code = 200
    fake.json.return_value = {"response": "def add(a, b): return a + b"}

    with patch("llm.client.requests.post", return_value=fake) as mock_post:
        result = generate("write add(a, b)", seed=3)

    assert result == "def add(a, b): return a + b"                                  # what the fake reply contained
    assert mock_post.call_args.args[0] == "http://localhost:11434/api/generate"             # the Ollama URL
    assert mock_post.call_args.kwargs["json"] == build_payload("write add(a, b)", seed=3)      # the payload that was sent