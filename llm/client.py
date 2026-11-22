MODEL = "qwen2.5-coder:3b"

def build_payload(prompt, seed, temperature=0.2):
    return {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature, "seed": seed},
    }