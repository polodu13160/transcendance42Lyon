from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base


t_get_differents_answers = Table(
    'get_differents_answers', Base.metadata,
    Column('id_event', Integer, primary_key=True),
    Column('id_answer', Integer, primary_key=True),
    ForeignKeyConstraint(['id_answer'], ['answers.id_answer'], name='get_differents_answers_id_answer_fkey'),
    ForeignKeyConstraint(['id_event'], ['events.id_event'], name='get_differents_answers_id_event_fkey'),
    PrimaryKeyConstraint('id_event', 'id_answer', name='get_differents_answers_pkey')
)