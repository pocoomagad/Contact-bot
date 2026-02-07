from fastapi import FastAPI
import uvicorn

from api.config import app_settings

from fastapi.responses import ORJSONResponse

app = FastAPI(
    title="ContactApi",
    summary="https://github.com/pocoomagad/Contact-bot",
    default_response_class=ORJSONResponse
)

@app.get("/healthcheck")
async def healthcheck():
    return {
        "app": "OK"
    }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=app_settings.API_HOST,
        port=app_settings.API_PORT
    )