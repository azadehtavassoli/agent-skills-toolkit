from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Typed settings class for FastAPI app.
    """
    PROJECT_NAME: str = "FastAPI App"
    API_VERSION: str = "0.1.0"

    # Cors origins, production/test settings
    CORS_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
