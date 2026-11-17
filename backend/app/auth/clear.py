from app.models.classes import Users, UserSession
from app.models.base import SessionLocal

def clear_users_tab():
    with SessionLocal() as db:
        db.query(Users).delete()
        db.commit()

def clear_usersession_tab():
    with SessionLocal() as db:
        db.query(UserSession).delete()
        db.commit()