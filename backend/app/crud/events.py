from sqlalchemy.orm import Session
from app.models.models import Event
from app.models.models import t_get_differents_answers_principal

def getAllEvent(db: Session, skip: int = 0, limit: int = 100):
    if limit == 0:
        return db.query(Event).all()
    return (db.query(Event).
            offset(skip)
            .limit(100))

def getEvent(db: Session, id: int):
    return (db.query(Event)
            .filter(Event.id_event == id)
            .first())

def getEventByCategory(db: Session, id: int):
    return (db.query(Event)
            .filter(Event.id_cat == id)
            .all())

def getEventByAnswer(db: Session, id: int):
    return (
        db.query(Event)
        .join(t_get_differents_answers_principal)
        .filter(t_get_differents_answers_principal.c.id_answer == id)
        .all()
    )

def getEventByStatus(db: Session, id: int):
    return (
        db.query(Event)
        .filter(Event.id_status == id)
        .all()
    )




