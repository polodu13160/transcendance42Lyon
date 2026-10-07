from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base


t_liked_users = Table(
    'liked_users', Base.metadata,
    Column('id_user_id_user', Integer, primary_key=True),
    Column('id_user_id_user_liked', Integer, primary_key=True),
    ForeignKeyConstraint(['id_user_id_user'], ['users.id_user'], name='liked_users_id_user_id_user_fkey'),
    ForeignKeyConstraint(['id_user_id_user_liked'], ['users.id_user'], name='liked_users_id_user_id_user_liked_fkey'),
    PrimaryKeyConstraint('id_user_id_user', 'id_user_id_user_liked', name='liked_users_pkey')
)
