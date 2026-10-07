from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.main import get_db
from app.crud import subevents

router = APIRouter(
    prefix="/subevents",
    tags=["events"],
)

@router.get("/", name="getAll", description="au lieu de mettre 0 c possible de chercher comme ca aussi")
@router.get(path="/{page}", description="si page = 0 alors la requete retourne tous les subevents, sinon il donne de 100 par 100")
async def read_all_subevents(page: int = 0, db: Session = Depends(get_db)):
    if page == 0:
        return subevents.getAllEvent(db, 0, 0)
    else:
        return subevents.getAllEvent(db, page * 100, 100)


@router.get("/answers/{id}", name="getByAnswer", description="donner id de la question")
async def read_subevents_with_id_answer(id: int, db: Session = Depends(get_db)):
    value = subevents.getEventByAnswer(db, id)
    if not value:
        raise HTTPException(status_code=404, detail="Item not found")
    return value


@router.get("/event/{id}", name="getByEvent", description="donner id de l'event")
async def read_subevents_with_id_cat(id: int, db: Session = Depends(get_db)):
    return subevents.getSubeventsByEvent(db, id)


@router.get("/status/{id}", name="getByUser", description="donner id de l'user")
async def read_subevents_with_id_user(id: int, db: Session = Depends(get_db)):
    return subevents.getEventByStatus(db, id)