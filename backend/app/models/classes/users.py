from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base




class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        ForeignKeyConstraint(['id_level'], ['leveluser.id_level'], name='users_id_level_fkey'),
        PrimaryKeyConstraint('id_user', name='users_pkey'),
        UniqueConstraint('id_wallet', name='users_id_wallet_key'),
        UniqueConstraint('nickname', name='users_nickname_key')
    )

    id_user: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    nickname: Mapped[str] = mapped_column(String(50), nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    date_creation: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False)
    id_level: Mapped[int] = mapped_column(Integer, nullable=False)
    bio: Mapped[Optional[str]] = mapped_column(String(300))
    id_wallet: Mapped[Optional[int]] = mapped_column(Integer)

    category: Mapped[list['Category']] = relationship('Category', secondary='liked_category', back_populates='users')
    events: Mapped[list['Events']] = relationship('Events', secondary='liked_events', back_populates='users')
    leveluser: Mapped['Leveluser'] = relationship('Leveluser', back_populates='users')
    id_user_user_liked: Mapped[list['Users']] = relationship('Users', secondary='liked_users', primaryjoin=lambda: Users.id_user == t_liked_users.c.id_user_id_user, secondaryjoin=lambda: Users.id_user == t_liked_users.c.id_user_id_user_liked, back_populates='id_user_user')
    id_user_user: Mapped[list['Users']] = relationship('Users', secondary='liked_users', primaryjoin=lambda: Users.id_user == t_liked_users.c.id_user_id_user_liked, secondaryjoin=lambda: Users.id_user == t_liked_users.c.id_user_id_user, back_populates='id_user_user_liked')
    bet: Mapped[list['Bet']] = relationship('Bet', back_populates='users')
    commentaire: Mapped[list['Commentaire']] = relationship('Commentaire', back_populates='users')
    commentaire_: Mapped[list['Commentaire']] = relationship('Commentaire', secondary='liked_comment', back_populates='users_')

