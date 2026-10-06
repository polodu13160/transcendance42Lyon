from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.main import get_db
from app.crud import events

router = APIRouter(
    prefix="/events",
    tags=["events"],
)

@router.get("/", name="getAll", description="au lieu de mettre 0 c possible de chercher comme ca aussi")
@router.get(path="/{page}", description="si page = 0 alors la requete retourne tous les events, sinon il donne de 100 par 100")
async def read_all_events(page: int = 0, db: Session = Depends(get_db)):
    if page == 0:
        return events.getAllEvent(db, 0, 0)
    else:
        return events.getAllEvent(db, page * 100, 100)


@router.get("/answers/{id}", name="getByAnswer", description="donner id de la question")
async def read_events_with_id_answer(id: int, db: Session = Depends(get_db)):
    value = events.getEventByAnswer(db, id)
    if not value:
        raise HTTPException(status_code=404, detail="Item not found")
    return value


@router.get("/category/{id}", name="getByCat", description="donner id de l'event")
async def read_events_with_id_cat(id: int, db: Session = Depends(get_db)):
    return events.getEventByCategory(db, id)


@router.get("/status/{id}", name="getByUser", description="donner id de l'user")
async def read_events_with_id_user(id: int, db: Session = Depends(get_db)):
    return events.getEventByStatus(db, id)