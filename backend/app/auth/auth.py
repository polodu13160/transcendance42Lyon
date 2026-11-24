from app.models.base import SessionLocal
from app.models import Users
from app.auth.sessions import create_session
from argon2.exceptions import VerifyMismatchError
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
import zon
from zon.error import ZonError
from argon2 import PasswordHasher

# zon for checking enail format
# argon2 for hash password and verify the hash 

def create_user(firstname, lastname, nickname, email: str, password: str)-> tuple [Users, str] | None:
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
        token = create_session(new_user.id_user)
        return new_user, token

# def verify_email()-> bool: # Implement email verification ? 
#     return True

def mailAuth(mail: str, password: str) ->tuple[Users, str]:
    ph = PasswordHasher()
    user = None
    with SessionLocal() as db: # To have an instance of SessionLocal
            user = db.scalar(
                select(Users).where(Users.user_email == mail)
            )
    if user is None:
        raise(VerifyMismatchError())   
    ph.verify(user.password_hash, password) 
    token = create_session(user.id_user)
    return user, token
    
def nicknameAuth(nickname: str, password: str) ->tuple[Users, str]:
    ph = PasswordHasher()
    user = None
    with SessionLocal() as db: # To have an instance of SessionLocal
            user = db.scalar(
                select(Users).where(Users.nick_name == nickname)
            )
    if user is None:
        raise(VerifyMismatchError())   
    ph.verify(user.password_hash, password) 
    token = create_session(user.id_user)
    return user, token
    
# def logout(token: )
