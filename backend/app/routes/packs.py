
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

import datetime
from app.schemas.colors import Colors
import random
from datetime import timezone




# POST /api/v1/auth/login


routerPack = APIRouter(
    prefix="/packs",
    responses={404: {"page": "Not found"}},
)

def range_no_duplicate_in_list(list_selected: list[Cards], list_no_duplicate: list[Cards]):
    value_selected = random.randrange(len(list_selected))
    while (1):
        if (list_selected[value_selected] in list_no_duplicate):
            value_selected = random.randrange(len(list_selected))
        else:
            break
    
    return list_selected[value_selected]



def unpack(request : Request, user: Users, if_first_pack: bool):
        
    cards_user: list[Card_user_schema] = []
    cards_selected: list[Cards] = [] 
    card: Cards
    with SessionLocal() as session:
        card: Cards
        if if_first_pack: 
            #10 : 1 gold, 2 violet, 3 rare, 4 aleatoires 
            for i in range(10):
                if i == 0:
                    card = range_no_duplicate_in_list(request.app.state.list_gold, cards_selected)
                elif i < 3:
                    card = range_no_duplicate_in_list(request.app.state.list_purple, cards_selected)
                elif i < 6:
                    card = range_no_duplicate_in_list(request.app.state.list_blue, cards_selected)
                else:
                    card = range_no_duplicate_in_list(request.app.state.list_cards, cards_selected)    
                card_get_exchange = Get_Exchanges(id_card = card.id_card, id_user = user.id_user, is_shiny = (random.randrange(20) == 5) , auction_bet = card.value_exchange, time_acquisition = datetime.datetime.now(timezone.utc))
                session.add(card_get_exchange)
                cards_user.append(Card_user_schema(card=card, card_user=card_get_exchange))
                cards_selected.append(card)
                
        else:
          
            for i in range(10):
                card = range_no_duplicate_in_list(request.app.state.list_cards, cards_selected)       
                card_get_exchange = Get_Exchanges(id_card = card.id_card, id_user = user.id_user, is_shiny = (random.randrange(20) == 5) , auction_bet = card.value_exchange, time_acquisition = datetime.datetime.now(timezone.utc))
                session.add(card_get_exchange)
                cards_user.append(Card_user_schema(card=card, card_user=card_get_exchange))
                cards_selected.append(card)
        user.date_free_pack = datetime.datetime.now(timezone.utc) + datetime.timedelta(milliseconds=10000)
        session.add(user)
        session.commit()
        return cards_user



    

@routerPack.get("/", description="""if is good time for open pack
**Header required:**
`Authorization: Bearer <TOKENSHASH>`"""
)
async def check_free_pack(current_user: Annotated[Users, Depends(get_current_user)]):
    if (current_user.date_free_pack == current_user.date_created):
        return {"get": {"get_free_pack": True, "date_new_pack": current_user.date_free_pack.strftime("%d/%m/%Y, %H:%M:%S")}}        
    elif (current_user.date_free_pack < datetime.datetime.now(timezone.utc)):
        return {"get": {"get_free_pack": False, "date_new_pack": current_user.date_free_pack.strftime("%d/%m/%Y, %H:%M:%S")}} 
    else:
        return {"get": {"get_free_pack": False, "date_new_pack": current_user.date_free_pack.strftime("%d/%m/%Y, %H:%M:%S")}}
    







@routerPack.post(
    "/free",
    description="""Give 10 cards in sorted of 0 to 4, one pack per day per account.

**Header required:**
`Authorization: Bearer <TOKENSHASH>`"""
)
async def free_pack(request: Request, current_user: Annotated[Users, Depends(get_current_user)]):
    cards = None
    if (current_user.date_free_pack == current_user.date_created):
        cards = unpack(request, current_user, True)
    elif (current_user.date_free_pack < datetime.datetime.now(timezone.utc)):
        cards = unpack(request, current_user, False)
    else:
        raise HTTPException(403, {'detail' :"user can not longer open free pack today", 
                                  'date_new_pack' : current_user.date_free_pack.strftime("%d/%m/%Y, %H:%M:%S")})  
    cards.sort(key=lambda x: x.card.colors)
    return {"pack": cards, "get": {"get_free_pack": False, "date_new_pack": current_user.date_free_pack.strftime("%d/%m/%Y, %H:%M:%S")}}

    







@routerPack.post(
    "/buy",
    description="""Give 10 cards in sorted of 0 to 4. no required money

**Header required:**
`Authorization: Bearer <TOKENSHASH>`"""
)
async def buy_pack(request:Request, current_user: Annotated[Users, Depends(get_current_user)]):
    #api crypto
    cards = unpack(request, current_user, False)
    cards.sort(key=lambda x: x.card.colors)
    return {"pack": cards, "get": {"get_free_pack": False, "date_new_pack": current_user.date_free_pack.strftime("%d/%m/%Y, %H:%M:%S")}}



