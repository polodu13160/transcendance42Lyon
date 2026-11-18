from app.models.base import SessionLocal
from app.models import Users
from app.auth.sessions import create_session
from argon2.exceptions import VerifyMismatchError
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
import zon
from zon.error import ZonError
from argon2 import PasswordHasher
from sqlalchemy.orm import Session

# zon for checking enail format
# argon2 for hash password and verify the hash 

def create_user(db: Session, firstname : str, lastname : str, nickname : str, email: str, password: str, id_wallet: int | None = None)-> tuple [Users, str] | None:
    ph = PasswordHasher()
    new_user = Users(
        last_name = lastname,
        first_name = firstname,
        nick_name = nickname,
        user_email = email,
        password_hash = ph.hash(password),
        id_wallet = id_wallet
    )
    db.add(new_user)
    db.commit()
    # Check double emails
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
    
            



# def auth(id: str, password: str) -> tuple [Users, str] | None: # id may be the email or the nickname
#     ph = PasswordHasher() # New instance of PassWordHasher
#     with SessionLocal() as db: # To have an instance of SessionLocal
#         user = db.scalars(
#             select(Users).where(Users.user_email == id)
#         ).first()
#         if user is None or user.password_hash is None:# or user.is_email_verified == False: # Uncomment if the email verification is implemented
#             user = db.scalars(
#                         select(Users).where(Users.nick_name == id)
#                     ).first()
#         if user is None or user.password_hash is None:# or user.is_email_verified == False: # Uncomment if the email verification is implemented
#             raise(VerifyMismatchError())
#         ph.verify(user.password_hash, password) # Matching the password with the hash stocked
#         token = create_session(user.id_user)
#         return user, token

# def delete_user():
