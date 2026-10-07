from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = (
        PrimaryKeyConstraint('id_cat', name='category_pkey'),
    )

    id_cat: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(String(100))

    users: Mapped[list['Users']] = relationship('Users', secondary='liked_category', back_populates='category')
    events: Mapped[list['Events']] = relationship('Events', back_populates='category')
