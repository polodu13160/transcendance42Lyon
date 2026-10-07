from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base


class Commentaire(Base):
    __tablename__ = 'commentaire'
    __table_args__ = (
        ForeignKeyConstraint(['id_user'], ['users.id_user'], name='commentaire_id_user_fkey'),
        PrimaryKeyConstraint('id_comment', name='commentaire_pkey')
    )

    id_comment: Mapped[int] = mapped_column(Integer, primary_key=True)
    comment: Mapped[str] = mapped_column(String(1000), nullable=False)
    id_user: Mapped[int] = mapped_column(Integer, nullable=False)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))

    users: Mapped['Users'] = relationship('Users', back_populates='commentaire')
    events: Mapped[list['Events']] = relationship('Events', secondary='get_comment_for_events', back_populates='commentaire')
    users_: Mapped[list['Users']] = relationship('Users', secondary='liked_comment', back_populates='commentaire_')
