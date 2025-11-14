FROM python:3.12.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=/root/.local/bin:$PATH

RUN apt update && \
    apt install curl -y && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false

WORKDIR /proj

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry install --no-root

COPY ./ ./
