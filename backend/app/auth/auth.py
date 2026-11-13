from app.models.base import SessionLocal
from app.models import Users
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
import zon
from zon.error import ZonError

def create_user(firstname, lastname, nickname, email: str, password: str)-> Users | None:
    validator = zon.string().email()
    try:
        validator.validate(email)
    except ZonError:
        return None
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
        print(f"An new user has been created !")
        return new_user

# def verify_email()-> bool:
#     return True

def auth(id: str, password: str) -> bool:
    ph = PasswordHasher()
    with SessionLocal() as db:
        user = db.scalars(
            select(Users).where(Users.user_email == id)
        ).first()
        if user is None or user.password_hash is None:# or user.is_email_verified == False:
            user = db.scalars(
                        select(Users).where(Users.nick_name == id)
                    ).first()
        if user is None or user.password_hash is None:# or user.is_email_verified == False:
            print(f"Error: Wrong email/identifier or password")
            return False
        try:
            ph.verify(user.password_hash, password)
            print(f"Authentification succes")
        except VerifyMismatchError:
            print(f"Error: Wrong email/identifier or password")
            return False
        return True