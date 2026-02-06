from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class DatabaseConfig(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_NAME: str
    PORT: int

    model_config = SettingsConfigDict(case_sensitive=True)

database_config = DatabaseConfig()