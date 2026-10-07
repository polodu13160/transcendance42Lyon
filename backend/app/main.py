from fastapi import FastAPI, dependencies
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from .models.class.base import SessionLocal

load_dotenv()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



    
app = FastAPI(title="Bdd")

from .routers import bet, events

app.include_router(bet.router)
app.include_router(events.router)






@app.get("/")
def read_root():
    return {"Bravo tu t'es connecté a l'api"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    q = "kdfsjkdfjkdfjkjdf"
    return {"item_id": item_id, "q": q}