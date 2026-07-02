import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "DevMind AI"

    VERSION = "1.0.0"

    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "claude-sonnet-4"
    )


settings = Settings()