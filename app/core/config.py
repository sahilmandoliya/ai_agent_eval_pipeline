import os

class Settings:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")

    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite+aiosqlite:///{DB_PATH}")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == "true"
    USE_LOCAL_LLM = os.getenv("USE_LOCAL_LLM", "false").lower() == "true"

settings = Settings()
