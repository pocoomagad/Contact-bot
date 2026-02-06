import asyncio
import uvicorn

from logging import getLogger

logger = getLogger(__name__)

def run_api() -> None:
    try:
        uvicorn.run(
            "api.app:app",
            reload=True
        )
        logger.info("API запущен")
    except Exception as e:
        logger.fatal(e)

def run_bot() -> None:
    ...

if __name__ == "__main__":
    run_api()
    run_bot()