from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base



t_get_comment_for_events = Table(
    'get_comment_for_events', Base.metadata,
    Column('id_event', Integer, primary_key=True),
    Column('id_comment', Integer, primary_key=True),
    ForeignKeyConstraint(['id_comment'], ['commentaire.id_comment'], name='get_comment_for_events_id_comment_fkey'),
    ForeignKeyConstraint(['id_event'], ['events.id_event'], name='get_comment_for_events_id_event_fkey'),
    PrimaryKeyConstraint('id_event', 'id_comment', name='get_comment_for_events_pkey')
)
