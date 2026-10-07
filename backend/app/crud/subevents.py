from sqlalchemy.orm import Session
from app.models.models import Subevents, Event
from app.models.models import t_get_differents_answers_secondary

def getAllSubevents(db: Session, skip: int = 0, limit: int = 100):
    if limit == 0:
        return db.query(Subevents).all()
    return (db.query(Subevents).
            offset(skip)
            .limit(100))

def getSubevents(db: Session, id: int):
    return (db.query(Subevents)
            .filter(Subevents.id_event == id)
            .first())

def getSubeventsByEvent(db: Session, id: int):
    return (db.query(Subevents)
            .filter(Subevents.id_event == id)
            .all())

def getSubeventsByAnswer(db: Session, id: int):
    return (
        db.query(Subevents)
        .join(t_get_differents_answers_secondary)
        .filter(t_get_differents_answers_secondary.c.id_answer == id)
        .all()
    )

def getSubeventsByStatus(db: Session, id: int):
    return (
        db.query(Subevents)
        .filter(Subevents.id_status == id)
        .all()
    )




