from backend.services.claude_service import ClaudeService


class LLMService:
    """
    Main LLM router.
    Currently uses Claude.
    Later this can route to Gemini, Ollama, etc.
    """

    def __init__(self):
        self.claude = ClaudeService()

    def generate_response(self, prompt: str) -> str:
        return self.claude.chat(prompt)


# Singleton instance
llm_service = LLMService()