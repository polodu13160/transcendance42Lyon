from fastapi import FastAPI, dependencies
from sqlalchemy.orm import Session
from app.core.env import ENVIRONMENT
from app.factories.users_factories import createUsersFactory
from contextlib import asynccontextmanager
import subprocess
from sqlalchemy_utils import create_database, database_exists
from app.scripts.recover_igdb import run
from app.models.base import engine




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
            print("Bdd data cards createds with success")
            if (ENVIRONMENT != 'PROD'):
                createUsersFactory(10)
        yield
    except Exception as e:
        print(e)
    finally:
        pass

app = FastAPI(title="Bdd", lifespan=lifespan)






@app.get("/")
def read_root():
    return {"Bravo tu t'es connecté a l'api"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    q = "kdfsjkdfjkdfjkjdf"
    return {"item_id": item_id, "q": q}