FROM python:3.11.11-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=/root/.local/bin:$PATH


RUN apt update && \
    apt install curl -y && \
    curl -sSL https://install.python-poetry.org | python3.11 - && \
    poetry config virtualenvs.create false


WORKDIR /proj

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . .


EXPOSE 8000
