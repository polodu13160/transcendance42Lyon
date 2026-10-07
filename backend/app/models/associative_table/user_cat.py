from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base




t_liked_category = Table(
    'liked_category', Base.metadata,
    Column('id_user', Integer, primary_key=True),
    Column('id_cat', Integer, primary_key=True),
    ForeignKeyConstraint(['id_cat'], ['category.id_cat'], name='liked_category_id_cat_fkey'),
    ForeignKeyConstraint(['id_user'], ['users.id_user'], name='liked_category_id_user_fkey'),
    PrimaryKeyConstraint('id_user', 'id_cat', name='liked_category_pkey')
)
