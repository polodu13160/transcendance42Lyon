# from pydantic import BaseModel, EmailStr, Field, ConfigDict,TypeAdapter,PrivateAttr, ValidationError, model_validator
# from typing import Annotated
# from fastapi import HTTPException, status, Request
# from app.models import Users, Cards, Get_Exchanges
# from app.schemas.Cards import Card_user_schema
# import datetime
# from app.auth.auth import mailAuth, nicknameAuth, create_user
# from fastapi import APIRouter, Depends
# from sqlalchemy import select
# from sqlalchemy.exc import IntegrityError
# from app.models.base import SessionLocal
# from app.routes.auth import get_current_user
# import enum
# from app.models import Get_Exchanges

# import datetime
# from app.schemas.colors import Colors
# import random
# from datetime import timezone


# from enum import StrEnum

# class ModelSort(StrEnum):
#     franchise = "franchise"
#     name_card = "name_card"
#     genre = ""

# class EnumWay(StrEnum):
#     asc = 'asc'
#     desc = 'desc'



# # POST /api/v1/auth/login


# routerCollection = APIRouter(
#     prefix="/collection",
#     responses={404: {"page": "Not found"}},
# )

# def strtobool (val):
#     """Convert a string representation of truth to true (1) or false (0).
#     True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
#     are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
#     'val' is anything else.
#     """
#     val = val.lower()
#     if val in ('y', 'yes', 't', 'true', 'on', '1'):
#         return 1
#     elif val in ('n', 'no', 'f', 'false', 'off', '0'):
#         return 0
#     else:
#         raise ValueError(f"invalid truth value {val}")


# class CollectionFilterParams(BaseModel):


#     franchise : str | None = None
#     way: EnumWay = EnumWay.asc           
#     is_shiny: bool | None = None   
#     is_dlc: bool | None = None
#     genre: str | None = None
#     colors : int | None = None       
#     limit: int = 20
#     offset: int = 0

#     #https://pydantic.dev/docs/validation/dev/concepts/validators/




# @routerCollection.get()





# @routerCollection.get(
#     "",
#     description="""

# **Header required:**
# `Authorization: Bearer <TOKENSHASH>`"""
# )
# async def print_collection(request:Request, current_user: Annotated[Users, Depends(get_current_user)]):
#     #api crypto
#     # with SessionLocal as session:
#     #     query = select(Get_Exchanges).join(Cards, Get_Exchanges.id_card == Cards.id_card).filter(Get_Exchanges.id_user == current_user.id_user)
#     #     for sort in sort_by:
#     #         if (sort.keys() == ModelSort.franchise):
#     #             query.filter(Cards.name_franchise == sort)
#     #         elif (sort.keys() == ModelSort.is_shiny):
#     #             value:bool = strtobool(sort)
#     #             query.filter(Get_Exchanges.is_shiny == value)
#     #         elif (sort.keys() == ModelSort.colors):
#     #             query.filter(Cards.colors == sort)
#     #     get_exchanges_cards = session.scalars(query)
#     #     print(get_exchanges_cards) 

        

