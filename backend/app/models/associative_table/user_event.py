from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base



t_liked_events = Table(
    'liked_events', Base.metadata,
    Column('id_user', Integer, primary_key=True),
    Column('id_event', Integer, primary_key=True),
    ForeignKeyConstraint(['id_event'], ['events.id_event'], name='liked_events_id_event_fkey'),
    ForeignKeyConstraint(['id_user'], ['users.id_user'], name='liked_events_id_user_fkey'),
    PrimaryKeyConstraint('id_user', 'id_event', name='liked_events_pkey')
)
