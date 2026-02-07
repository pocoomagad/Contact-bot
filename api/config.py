from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import os

def get_env_file():
    root_dir = Path(__file__).resolve().parents[1]
    ENV = os.path.join(root_dir, ".env")
    return ENV

class ContactSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=get_env_file(), extra="ignore")

class AppSettings(ContactSettings):
    API_HOST: str
    API_PORT: str

app_settings = AppSettings()

class DatabaseConfig(ContactSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_NAME: str
    POSTGRES_PORT: int

    ENGINE_ECHO: bool
    ENGINE_PLUGINS: list[str]
    ENGINE_POOL_TIMEOUT: int
    ENGINE_POOL_SIZE: int
    ENGINE_MAX_OVERFLOW: int

database_config = DatabaseConfig()

class AlembicConfig(ContactSettings):
    ...