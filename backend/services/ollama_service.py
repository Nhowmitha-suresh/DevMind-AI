import ollama

MODEL = "qwen2.5-coder:7b"

def generate_response(message: str):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response["message"]["content"]