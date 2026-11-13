from app.models.base import SessionLocal
from app.models import Users
from argon2 import PasswordHasher
from sqlalchemy.exc import IntegrityError

def create_user(firstname, lastname, nickname, email: str, password: str)-> Users | None:
    email = email.strip().lower() #normalization
    ph = PasswordHasher()
    new_user = Users(
        last_name = lastname,
        first_name = firstname,
        nick_name = nickname,
        user_email = email,
        password_hash = ph.hash(password),
    )
    with SessionLocal() as db:
        db.add(new_user)
        try:
            db.commit()
        except IntegrityError: # Check double emails
            db.rollback()
            return None
        db.refresh(new_user)
        return new_user

# def verify_email()-> bool:
#     return True

def auth(email: str, password: str)-> bool:
    email = email.strip().lower()
    ph = PasswordHasher()
    password = ph.hash(password)
    with SessionLocal() as db:
        try:
            target = db.query(Users).filter(Users.user_email)
        except IntegrityError:
            print(f"Error: Wrong email or password")
            return False
        if ph.verify(target.password_hash, password) :
            return True
        else:
            print(f"Error: Wrong email or password")
            return False
