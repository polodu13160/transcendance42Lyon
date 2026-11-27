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
from app.models.base import get_db
from sqlalchemy.orm import Session
from app.routes.auth import get_current_user
import enum
from app.models import Get_Exchanges
from app.models.base import SessionLocal, get_db

import datetime
from app.schemas.colors import Colors
import random
from datetime import timezone




routerUtils= APIRouter(
    prefix="/utils",
    responses={404: {"page": "Not found"}},
)

@routerUtils.get("/me/genres")
def me_genres(current_user: Annotated[Users, Depends(get_current_user)], session : Annotated[Session, Depends(get_db)]):

    genres_cards = session.scalars(select(Cards.genre).join(Get_Exchanges, Get_Exchanges.id_card == Cards.id_card).filter(Get_Exchanges.id_user == current_user.id_user).group_by(Cards.genre)).all()
    genres: list[str] = []
    for genres_card in genres_cards:
        if genres_card is not None:
            for genre in genres_card:
                if (genre not in genres):
                    genres.append(genre)
    return genres

    
@routerUtils.get("/me/colors")
def me_colors(current_user: Annotated[Users, Depends(get_current_user)], session : Annotated[Session, Depends(get_db)]):

    colors = session.scalars(select(Cards.colors).join(Get_Exchanges, Get_Exchanges.id_card == Cards.id_card).filter(Get_Exchanges.id_user == current_user.id_user).group_by(Cards.colors)).all()
    return colors

@routerUtils.get("/me/franchises")
def me_franchises(current_user: Annotated[Users, Depends(get_current_user)], session: Annotated[Session, Depends(get_db)]):
    
    franchises = session.scalars(select(Cards.name_franchise).join(Get_Exchanges, Get_Exchanges.id_card == Cards.id_card).filter(Get_Exchanges.id_user == current_user.id_user).group_by(Cards.name_franchise)).all()
    return franchises


@routerUtils.get("/all/genres")
def genres(session: Annotated[Session, Depends(get_db)]):
   
    genres_cards = session.scalars(select(Cards.genre).group_by(Cards.genre)).all()
    genres: list[str] = []
    for genres_card in genres_cards:
        if genres_card is not None:
            for genre in genres_card:
                if (genre not in genres):
                    genres.append(genre)
    return genres
  
@routerUtils.get("/all/colors")
def colors(session: Annotated[Session, Depends(get_db)]):
    colors = session.scalars(select(Cards.colors).group_by(Cards.colors)).all()
    return colors

@routerUtils.get("/all/franchises")
def franchises(session: Annotated[Session, Depends(get_db)]):
    franchises = session.scalars(select(Cards.name_franchise).group_by(Cards.name_franchise)).all()
    return franchises

@routerUtils.get("/search/me/{name_card}")
def search_my_cards(name_card: str, current_user: Annotated[Users, Depends(get_current_user)], session: Annotated[Session, Depends(get_db)]):
    stmt = (
        select(Cards)
        .join(Get_Exchanges, Get_Exchanges.id_card == Cards.id_card)
        .where(
            Get_Exchanges.id_user == current_user.id_user,
            Cards.name.ilike(f"%{name_card}%"),  # Remplace 'name' par le vrai nom de ta colonne
        )
    )
    return session.scalars(stmt).all()


