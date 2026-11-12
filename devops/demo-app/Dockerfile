FROM astral/uv:python3.12-bookworm-slim

WORKDIR /app

# Dépendances d'abord (cache Docker : ne se réinstalle que si ces fichiers changent)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY main.py .

EXPOSE 8000

CMD ["uv", "run", "--no-sync", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]