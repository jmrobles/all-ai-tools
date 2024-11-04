from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Tool RAG System"
    API_TOKEN: str
    DATABASE_URL: str
    OPENAI_API_KEY: str
    LOG_LEVEL: str = "INFO"
    TELEGRAM_BOT_TOKEN: str
    NEMO_GUARDRAILS_CONFIG_PATH: Path = Path(__file__).parent.parent / "guardrails"
    USE_WEBHOOK: bool = False
    WEBHOOK_URL: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
