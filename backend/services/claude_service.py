import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class ClaudeService:
    def __init__(self):
        self.client = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.model = os.getenv("MODEL_NAME", "claude-sonnet-4")

    def chat(self, message: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.content[0].text