from fastapi import FastAPI, dependencies
from dotenv import load_dotenv
from sqlalchemy.orm import Session

load_dotenv()





    
app = FastAPI(title="Bdd")

from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)





@app.get("/")
def read_root():
    return {"Bravo tu t'es connecté a l'api"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    q = "kdfsjkdfjkdfjkjdf"
    return {"item_id": item_id, "q": q}
