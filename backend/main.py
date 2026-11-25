from fastapi import FastAPI, dependencies
from sqlalchemy.orm import Session
from app.core.env import ENVIRONMENT
from app.factories.users_factories import createUsersFactory
from contextlib import asynccontextmanager
import subprocess
from sqlalchemy_utils import create_database, database_exists
from app.scripts.recover_igdb import run
from app.models.base import engine, SessionLocal
from prometheus_fastapi_instrumentator import Instrumentator
from app.routes.auth import routerAuth
from app.routes.packs import routerPack
from app.routes.collections import routerCollection
from app.models import Cards
from sqlalchemy import select
from app.schemas.colors import Colors


list_cards: list[Cards]
list_gold: list[Cards]
list_purple: list[Cards]
list_blue: list[Cards]

@asynccontextmanager
async def lifespan(app: FastAPI):

    try:
        if not database_exists(engine.url):
            create_database(engine.url)
            print("Bdd created success")
            subprocess.run(["uv", "run", "alembic", "upgrade", "head"], 
                           check=True)
            print("Bdd tables created")
            run()
            print("Bdd data cards created with success")
            # if (ENVIRONMENT != 'PROD'):
            #     createUsersFactory(10)
        with SessionLocal() as session:
            app.state.list_cards = list(session.scalars(select(Cards)).all())
            app.state.list_gold = [card for card in app.state.list_cards  if card.colors == Colors.GOLD.value["id"]]
            app.state.list_purple  = [card for card in app.state.list_cards  if card.colors == Colors.PURPLE.value["id"]]
            app.state.list_blue = [card for card in app.state.list_cards  if card.colors == Colors.BLUE.value["id"]]
        yield
    except Exception as e:
        print(e)
    finally:
        pass

app = FastAPI(title="Bdd", lifespan=lifespan)
Instrumentator().instrument(app).expose(app)

prefix = '/api/v1'

app.include_router(router=routerAuth, prefix=prefix, tags=["auth"])
app.include_router(router=routerPack, prefix=prefix, tags=["pack"])
app.include_router(router=routerCollection, prefix=prefix, tags=["collection"])




# @app.get("/")
# def read_root():
#     return {"Bravo tu t'es connecté a l'api"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     q = "kdfsjkdfjkdfjkjdf"
#     return {"item_id": item_id, "q": q}