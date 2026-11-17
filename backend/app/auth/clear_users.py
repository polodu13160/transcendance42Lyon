from app.models.classes.Users import Users
from app.models.base import SessionLocal

def clear_users_tab():
    with SessionLocal() as db:
        db.query(Users).delete()
        db.commit()

clear_users_tab()