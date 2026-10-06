from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.main import get_db
from app.crud import bets

router = APIRouter(
    prefix="/bets",
    tags=["bets"],
)

@router.get("/", name="getAll", description="si page = 0 alors la requete retourne tous les paris, sinon il donne de 100 par 100")
@router.get(path="/{page}", description="si page = 0 alors la requete retourne tous les paris, sinon il donne de 100 par 100")
async def read_all_bets(page: int = 0, db: Session = Depends(get_db)):
    if page == 0:
        return bets.getAllBets(db, 0, 0)
    else:
        return bets.getAllBets(db, page * 100, 100)


@router.get("/answers/{id}", name="getByAnswer", description="donner id de la question")
async def read_bets_with_id_answer(id: int, db: Session = Depends(get_db)):
    value = bets.getBetsByAnswer(db, id)
    if not value:
        raise HTTPException(status_code=404, detail="Item not found")
    return value


@router.get("/events/{id}", name="getByEvent", description="donner id de l'event")
async def read_bets_with_id_event(id: int, db: Session = Depends(get_db)):
    return bets.getBetsByEvent(db, id)


@router.get("/users/{id}", name="getByUser", description="donner id de l'user")
async def read_bets_with_id_user(id: int, db: Session = Depends(get_db)):
    return bets.getBetByUser(db, id)