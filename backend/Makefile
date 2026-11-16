.PHONY: all

all:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync
	@read -p "Mettre en place la db (peut reset les donnees si deja en place) [y/N] : " response; \
	if [ "$$response" = "y" ] || [ "$$response" = "Y" ]; then \
		uv run alembic upgrade head; \
	fi
	uv add prometheus-fastapi-instrumentator
	uv run fastapi dev







##uv sync installe les dependances locales
#uv pip freeze > requirements.txt

#pour Jos : il est preferable de faire un 