from pydantic import BaseModel, EmailStr, Field, ConfigDict,TypeAdapter,PrivateAttr, ValidationError, model_validator
from typing import Annotated
from fastapi import HTTPException, status, Request
from app.models import Users, Cards, Get_Exchanges
from app.schemas.Cards import Card_user_schema
import datetime
from app.auth.auth import mailAuth, nicknameAuth, create_user
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.base import SessionLocal
from app.routes.auth import get_current_user
import enum
from app.models import Get_Exchanges

import datetime
from app.schemas.colors import Colors
import random
from datetime import timezone


from enum import StrEnum

class ModelSort(StrEnum):
    franchise = "franchise"
    name_card = "name_card"
    genre = ""

class EnumWay(StrEnum):
    asc = 'asc'
    desc = 'desc'


routerUtils= APIRouter(
    prefix="/utils",
    responses={404: {"page": "Not found"}},
)

@routerUtils.get("/me/genres")
def me_genres(current_user: Annotated[Users, Depends(get_current_user)]):
    pass
@routerUtils.get("/me/colors")
def me_colors(current_user: Annotated[Users, Depends(get_current_user)]):
    pass
@routerUtils.get("/me/franchises")
def me_franchises(current_user: Annotated[Users, Depends(get_current_user)]):
    pass

