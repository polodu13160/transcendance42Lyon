from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Bravo tu t'es connecté a l'api"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    q = "kdfsjkdfjkdfjkjdf"
    return {"item_id": item_id, "q": q}