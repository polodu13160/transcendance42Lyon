from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base

class Bet(Base):
    __tablename__ = 'bet'
    __table_args__ = (
        ForeignKeyConstraint(['id_answer'], ['answers.id_answer'], name='bet_id_answer_fkey'),
        ForeignKeyConstraint(['id_event'], ['events.id_event'], name='bet_id_event_fkey'),
        ForeignKeyConstraint(['id_status'], ['status.id_status'], name='bet_id_status_fkey'),
        ForeignKeyConstraint(['id_user'], ['users.id_user'], name='bet_id_user_fkey'),
        PrimaryKeyConstraint('id_bet', name='bet_pkey')
    )

    id_bet: Mapped[int] = mapped_column(Integer, primary_key=True)
    date_: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False)
    cote: Mapped[decimal.Decimal] = mapped_column(Numeric(25, 10), nullable=False)
    odds: Mapped[decimal.Decimal] = mapped_column(Numeric(25, 10), nullable=False)
    id_answer: Mapped[int] = mapped_column(Integer, nullable=False)
    id_status: Mapped[str] = mapped_column(String(50), nullable=False)
    id_event: Mapped[int] = mapped_column(Integer, nullable=False)
    id_user: Mapped[int] = mapped_column(Integer, nullable=False)

    answers: Mapped['Answers'] = relationship('Answers', back_populates='bet')
    events: Mapped['Events'] = relationship('Events', back_populates='bet')
    status: Mapped['Status'] = relationship('Status', back_populates='bet')
    users: Mapped['Users'] = relationship('Users', back_populates='bet')
