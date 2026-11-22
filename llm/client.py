import requests

MODEL = "qwen2.5-coder:3b"
OLLAMA_URL = "http://localhost:11434/api/generate"

def build_payload(prompt, seed, temperature=0.2):
    return {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature, "seed": seed},
    }

def generate(prompt, seed):
    payload = build_payload(prompt, seed)
    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    return response.json()["response"]
