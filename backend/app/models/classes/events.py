from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base




class Events(Base):
    __tablename__ = 'events'
    __table_args__ = (
        ForeignKeyConstraint(['id_cat'], ['category.id_cat'], name='events_id_cat_fkey'),
        ForeignKeyConstraint(['id_status'], ['status.id_status'], name='events_id_status_fkey'),
        PrimaryKeyConstraint('id_event', name='events_pkey'),
        UniqueConstraint('name', name='events_name_key')
    )

    id_event: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    name: Mapped[str] = mapped_column(String(300), nullable=False)
    date_creation: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False)
    id_cat: Mapped[int] = mapped_column(Integer, nullable=False)
    id_status: Mapped[str] = mapped_column(String(50), nullable=False)
    url_images: Mapped[Optional[str]] = mapped_column(String(1000))
    liked: Mapped[Optional[int]] = mapped_column(Integer)

    answers: Mapped[list['Answers']] = relationship('Answers', secondary='get_differents_answers', back_populates='events')
    category: Mapped['Category'] = relationship('Category', back_populates='events')
    status: Mapped['Status'] = relationship('Status', back_populates='events')
    users: Mapped[list['Users']] = relationship('Users', secondary='liked_events', back_populates='events')
    bet: Mapped[list['Bet']] = relationship('Bet', back_populates='events')
    commentaire: Mapped[list['Commentaire']] = relationship('Commentaire', secondary='get_comment_for_events', back_populates='events')




