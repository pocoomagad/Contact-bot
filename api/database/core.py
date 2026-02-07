from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine
from sqlalchemy import BigInteger

from api.config import database_config

def make_url(user: str, password: str, port: str, name: str):
    return f"postgresql+asyncpg://{user}:{password}@db:{port}/{name}"

def create_async_sqlalchemy_engine(sqlalchemy_config) -> AsyncEngine:

    url = make_url(
        user=sqlalchemy_config.POSTGRES_USER,
        password=sqlalchemy_config.POSTGRES_PASSWORD,
        port=sqlalchemy_config.POSTGRES_PORT,
        name=sqlalchemy_config.POSTGRES_NAME
    )

    engine_kw = {
        "echo": sqlalchemy_config.ENGINE_ECHO,
        "pool_timeout": config.ENGINE_POOL_TIMEOUT,
        "pool_size": config.ENGINE_POOL_SIZE,
        "max_overflow": config.ENGINE_MAX_OVERFLOW,
        "plugins": config.ENGINE_PLUGINS
    }

    return create_async_engine(url, **engine_kw)

engine = create_async_sqlalchemy_engine(database_config)

Session = async_sessionmaker(
    bind=engine,
    expire_on_commit=True
)