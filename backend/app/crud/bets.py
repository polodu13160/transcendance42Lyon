from sqlalchemy.orm import Session
from app.models.models import Bets

def getAllBets(db: Session, skip: int = 0, limit: int = 100):
    if limit == 0:
        return db.query(Bets).all()
    return db.query(Bets).offset(skip).limit(100)

def getBet(db: Session, id: int):
    return db.query(Bets).filter(Bets.id_bet == id).first()

def getBetsByEvent(db: Session, id: int):
    return db.query(Bets).filter(Bets.id_event == id).all()

def getBetsByAnswer(db: Session, id: int):
    return db.query(Bets).filter(Bets.id_answer == id).all()

def getBetByUser(db: Session, id: int):
    return db.query(Bets).filter(Bets.id_user == id).all()
