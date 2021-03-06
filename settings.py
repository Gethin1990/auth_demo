import secrets
from functools import lru_cache

from pydantic import BaseSettings

from entity.dto.setting import Environment

class Settings(BaseSettings):
    environment: Environment = "development"
    token_generator_secret_key: str = secrets.token_hex(64)
    access_token_expire_minutes: int = 120
    refresh_token_expire_minutes: int = 120
    api_disable_docs: bool = False
    api_debug: bool = True

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        use_enum_values = True


@lru_cache()
def get_settings():
    return Settings()