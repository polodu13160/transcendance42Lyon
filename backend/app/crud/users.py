from sqlalchemy.orm import Session
from app.models.models import Users
from app.models.models import t_get_differents_answers_secondary

def getAllUsers(db: Session, skip: int = 0, limit: int = 100):
    if limit == 0:
        return db.query(Users).all()
    return (db.query(Users).
            offset(skip)
            .limit(100))

def getUsers(db: Session, id: int):
    return (db.query(Users)
            .filter(Users.id_event == id)
            .first())

def getUsersByBets(db: Session, id: int):
    return (db.query(Users)
            .filter(Users.id_event == id)
            .all())

def getUsersByLiked(db: Session, id: int):
    return (
        db.query(Users)
        .join(t_get_differents_answers_secondary)
        .filter(t_get_differents_answers_secondary.c.id_answer == id)
        .all()
    )

def getUsersByStatus(db: Session, id: int):
    return (
        db.query(Users)
        .filter(Users.id_status == id)
        .all()
    )

