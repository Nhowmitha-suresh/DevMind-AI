import os

from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class ClaudeService:
    """
    Service responsible for communicating with the Anthropic Claude API.
    """

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.model = os.getenv("MODEL_NAME", "claude-sonnet-4")

        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found in environment variables."
            )

        self.client = Anthropic(api_key=self.api_key)

    def generate_response(
        self,
        user_message: str,
        system_prompt: str = "You are DevMind AI, an expert AI coding assistant."
    ) -> str:
        """
        Send a prompt to Claude and return the response.
        """

        try:

            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                temperature=0.7,
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            return response.content[0].text

        except Exception as e:
            raise Exception(f"Claude API Error: {str(e)}")