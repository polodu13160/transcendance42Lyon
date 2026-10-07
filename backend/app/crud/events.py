from sqlalchemy.orm import Session
from app.models import Events
from app.models import t_get_differents_answers

def getAllEvent(db: Session, skip: int = 0, limit: int = 100):
    if limit == 0:
        return db.query(Events).all()
    return (db.query(Events).
            offset(skip)
            .limit(100))

def getEvent(db: Session, id: int):
    return (db.query(Events)
            .filter(Events.id_event == id)
            .first())

def getEventByCategory(db: Session, id: int):
    return (db.query(Events)
            .filter(Events.id_cat == id)
            .all())

def getEventByAnswer(db: Session, id: int):
    return (
        db.query(Events)
        .join(t_get_differents_answers)
        .filter(t_get_differents_answers.c.id_answer == id)
        .all()
    )

def getEventByStatus(db: Session, id: int):
    return (
        db.query(Events)
        .filter(Events.id_status == id)
        .all()
    )




