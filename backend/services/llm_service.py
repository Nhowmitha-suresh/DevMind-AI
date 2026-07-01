import ollama

from config import MODEL_NAME


class LLMService:

    @staticmethod
    def generate(prompt: str):

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]