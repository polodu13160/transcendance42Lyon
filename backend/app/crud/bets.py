from sqlalchemy.orm import Session
from app.models import Bet

def getAllBets(db: Session, skip: int = 0, limit: int = 100):
    if limit == 0:
        return db.query(Bet).all()
    return db.query(Bet).offset(skip).limit(100)

def getBet(db: Session, id: int):
    return db.query(Bet).filter(Bet.id_bet == id).first()

def getBetsByEvent(db: Session, id: int):
    return db.query(Bet).filter(Bet.id_event == id).all()

def getBetsByAnswer(db: Session, id: int):
    return db.query(Bet).filter(Bet.id_answer == id).all()

def getBetByUser(db: Session, id: int):
    return db.query(Bet).filter(Bet.id_user == id).all()
