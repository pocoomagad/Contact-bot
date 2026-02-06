from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from api.database.config import database_config

url = f"""
    postgresql+asyncpg://{database_config.POSTGRES_USER}:
    {database_config.POSTGRES_PASSWORD}@db:
    {database_config.PORT}/{database_config.POSTGRES_NAME}
    """

async_engine = create_async_engine(
    url,
    echo=True,
    plugins=["geoalchemy2"]
)

Session = async_sessionmaker(async_engine, expire_on_commit=True)

class Base(DeclarativeBase):
    def __repr__(self):
        return f"{self.__class__.__name__}"