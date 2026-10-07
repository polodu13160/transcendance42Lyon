from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base
from app.models.classes.events import Events
from app.models.classes.bets import Bet



class Answers(Base):
    __tablename__ = 'answers'
    __table_args__ = (
        PrimaryKeyConstraint('id_answer', name='answers_pkey'),
    )

    id_answer: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    date_expiration: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    cote: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(25, 10))

    events: Mapped[list['Events']] = relationship('Events', secondary='get_differents_answers', back_populates='answers')
    bet: Mapped[list['Bet']] = relationship('Bet', back_populates='answers')