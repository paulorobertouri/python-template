FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

COPY app/ ./app/
COPY main.py ./

ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "./main.py"]
