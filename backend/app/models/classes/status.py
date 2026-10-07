from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base


class Status(Base):
    __tablename__ = 'status'
    __table_args__ = (
        PrimaryKeyConstraint('id_status', name='status_pkey'),
    )

    id_status: Mapped[str] = mapped_column(String(50), primary_key=True)
    name_status: Mapped[Optional[str]] = mapped_column(String(50))

    events: Mapped[list['Events']] = relationship('Events', back_populates='status')
    bet: Mapped[list['Bet']] = relationship('Bet', back_populates='status')