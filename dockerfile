FROM python:alpine
WORKDIR /contact_bot

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \ 
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache 

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root

COPY . .

RUN alembic revision autogenerate -m "create_tables" && alembic upgrade head

CMD [ "poetry", "run", "python", "-m", "api.app" ]