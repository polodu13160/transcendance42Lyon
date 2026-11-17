from app.models.classes import UserSession
from app.models.base import SessionLocal

def clear_usersession_tab():
    with SessionLocal() as db:
        db.query(UserSession).delete()
        db.commit()

clear_usersession_tab()