from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base



t_liked_comment = Table(
    'liked_comment', Base.metadata,
    Column('id_user', Integer, primary_key=True),
    Column('id_comment', Integer, primary_key=True),
    ForeignKeyConstraint(['id_comment'], ['commentaire.id_comment'], name='liked_comment_id_comment_fkey'),
    ForeignKeyConstraint(['id_user'], ['users.id_user'], name='liked_comment_id_user_fkey'),
    PrimaryKeyConstraint('id_user', 'id_comment', name='liked_comment_pkey')
)
