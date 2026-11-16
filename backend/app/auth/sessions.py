import hashlib
import secrets
from datetime import datetime, timedelta, timezone

from sqlalchemy import select

from app.models.base import SessionLocal
from app.models import Users, UserSession

SESSION_TTL = timedelta(days=1)

def _hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()

def _utcnow() -> datetime:
    return datetime.now(timezone.utc)

def create_session(user_id: int) -> str:
    token = secrets.token_urlsafe(32)
    with SessionLocal as db:
        db.add(UserSession(
            token_hash = _hash_token(token),
            user_id = user_id,
            expires_at = _utcnow() + SESSION_TTL,
        ))
        db.commit()
    return token

def get_user_from_token(token: str)-> Users | None:
    with SessionLocal as db:
        sess = db.scalars(
            select(UserSession).where(UserSession._hash_token == _hash_token(token))
        ).first
        if sess is None:
            return None
        expires_at = sess.expires_at
        if expires_at.tzinfo == None:
            expires_at == expires_at.replace(tzinfo=timezone.utc)
        if expires_at < _utcnow:
            db.delete(sess)
            db.commit()
            return None
        return db.get(Users, sess.user_id)

def delete_session(token: str)-> None:
    with SessionLocal as db:
        sess = db.scalars(
                    select(UserSession).where(UserSession._hash_token == _hash_token(token))
        ).first
        if sess is None:
            db.delete(sess)
            db.commit()