
from pydantic import BaseModel, EmailStr, Field, ConfigDict,TypeAdapter,PrivateAttr, ValidationError, model_validator
from typing import Annotated
from fastapi import HTTPException
from app.models import Users, Cards, Get_Exchanges
from app.schemas.Cards import Card_user_schema
import datetime
from app.auth.auth import mailAuth, nicknameAuth, create_user
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.base import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from app.auth.sessions import get_user_from_token
import datetime
from app.schemas.colors import Colors
import random


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")

with SessionLocal() as session:
    list_cards: list[Cards] = list(session.scalars(select(Cards)).all())
    list_gold: list[Cards] = [card.id_card for card in list_cards if card.colors == Colors.GOLD.value]
    list_purple: list[Cards] = [card.id_card for card in list_cards if card.colors == Colors.PURPLE.value]
    list_blue: list[Cards] = [card.id_card for card in list_cards if card.colors == Colors.BLUE.value]

# POST /api/v1/auth/login

async def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
    user = get_user_from_token(token)
    if user == None:
        raise HTTPException(401, 'error Token')



routerAuth = APIRouter(
    prefix="/packs",
    responses={404: {"page": "Not found"}},
)

def range_no_duplicate_in_list(list_selected: list[Cards], list_no_duplicate: list[Get_Exchanges]):
    value_selected = random.randrange(stop=list_selected.count())
    try:
        while (1):
            list_no_duplicate[value_selected]
            value_selected = random.randrange(stop=list_selected.count())
    except:
        return list_selected[value_selected]



def unpack(user: Users, if_first_pack: bool):
        
        cards_selected: list[Card_user_schema] = [] 
        card: Cards
        with SessionLocal() as session:
            if first_pack == True: #10 : 1 gold, 2 violet, 3 rare, 4 aleatoires 
                for i in range(10):
                    if i == 0:
                        card = range_no_duplicate_in_list(list_gold, cards_selected)
                    elif i < 3:
                        card = range_no_duplicate_in_list(list_purple, cards_selected)
                    elif i < 6:
                        card = range_no_duplicate_in_list(list_blue, cards_selected)
                    else:
                        card = range_no_duplicate_in_list(list_cards, cards_selected)    

                    if (random.randrange(stop=20) == 5):
                        card_get_exchange = Get_Exchanges(id_card = card.id_card, id_user = user.id_user, is_shiny = True)
                    else:
                        card_get_exchange = Get_Exchanges(id_card = card.id_card, id_user = user.id_user, is_shiny = False)
                    
                    cards_selected.append(Card_user_schema(card=card, card_user=Card_user_schema.card_user.model_validate(card_get_exchange)))
                    session.add(card_get_exchange)
            else:
              
                for i in range(10):
                    card = range_no_duplicate_in_list(list_cards, cards_selected)       
                    if (random.randrange(stop=20) == 5):
                        card_get_exchange = Get_Exchanges(id_card = card.id_card, id_user = user.id_user, is_shiny = True)
                    else:
                        card_get_exchange = Get_Exchanges(id_card = card.id_card, id_user = user.id_user, is_shiny = False)

                    cards_selected.append(Card_user_schema(card=card, card_user=Card_user_schema.card_user.model_validate(card_get_exchange)))
                    session.add(card_get_exchange)
            session.commit()
            return {cards_selected}



    







@routerAuth.post('/free', description="authentification user")
async def free_pack(current_user: Annotated[Users, Depends(get_current_user)]):
    cards = None
    if (current_user.date_free_pack == current_user.date_created):
        cards = unpack(current_user, True)
    elif (current_user.date_free_pack < datetime.datetime.now()):
        cards = unpack(current_user, False)
    elif cards == None:
        raise HTTPException(403, {'detail' :"user can not longer open free pack today", 
                                  'date_new_pack' : current_user.date_free_pack})  
    return cards


    







@routerAuth.post('/buy', description="authentification user")
async def buy_pack(current_user: Annotated[Users, Depends(get_current_user)]):
    #api crypto
    cards = unpack(current_user, False)
    return cards



