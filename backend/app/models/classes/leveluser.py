from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base



class Leveluser(Base):
    __tablename__ = 'leveluser'
    __table_args__ = (
        PrimaryKeyConstraint('id_level', name='leveluser_pkey'),
    )

    id_level: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    users: Mapped[list['Users']] = relationship('Users', back_populates='leveluser')

