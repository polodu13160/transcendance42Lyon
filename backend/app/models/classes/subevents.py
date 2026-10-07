from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base


class Subevents(Base):
    __tablename__ = 'subevents'
    __table_args__ = (
        ForeignKeyConstraint(['id_event'], ['events.id_event'], name='subevents_id_event_fkey'),
        PrimaryKeyConstraint('id_subevent', name='subevents_pkey')
    )

    id_subevent: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_event: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(300))
    url_images: Mapped[Optional[str]] = mapped_column(String(1000))
    name: Mapped[Optional[str]] = mapped_column(String(300))

    events: Mapped['Events'] = relationship('Events', back_populates='subevents')