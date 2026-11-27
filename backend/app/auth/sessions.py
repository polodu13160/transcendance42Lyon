import hashlib
import secrets
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session


from sqlalchemy import select

from app.models.base import SessionLocal
from app.models import Users, UserSession

SESSION_TTL = timedelta(days=1)

def create_session(user_id: int, db : Session) -> str:
    token = secrets.token_urlsafe(32) 
    db.add(UserSession(
        token_hash = hashlib.sha256(token.encode()).hexdigest(),
        user_id = user_id,
        expires_at = datetime.now(timezone.utc) + SESSION_TTL,
    ))
    db.commit()
    return token

def get_user_from_token(token: str, db: Session)-> Users | None:
    sess = db.scalars(
        select(UserSession).where(UserSession.token_hash == hashlib.sha256(token.encode()).hexdigest())
    ).first()
    if sess is None:
        return None
    expires_at = sess.expires_at
    if expires_at.tzinfo == None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)
    if expires_at < datetime.now(timezone.utc):
        db.delete(sess)
        db.commit()
        return None
    return db.get(Users, sess.user_id)

def delete_session(token: str, db: Session)-> None:
    sess = db.scalars(
                select(UserSession).where(UserSession.token_hash == hashlib.sha256(token.encode()).hexdigest())
    ).first()
    if sess:
        db.delete(sess)
        db.commit()