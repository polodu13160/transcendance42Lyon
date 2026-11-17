FROM astral/uv:python3.12-bookworm-slim

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /code

# Dépendances d'abord (cache Docker : ne se réinstalle que si ces fichiers changent)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# On copy le code
COPY alembic.ini main.py ./
COPY /app ./app/
COPY /alembic ./alembic/

# On installe le projet (pas obligatoire)
RUN uv sync --frozen --no-dev

# On crée un utilisateur pour que le container ne soit pas lancé en non-root
RUN useradd --create-home appuser && chown -R appuser /code
USER appuser

EXPOSE 8000

CMD ["uv", "run", "--no-sync", "fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]