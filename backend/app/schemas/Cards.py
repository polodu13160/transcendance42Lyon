 
from pydantic import BaseModel, AwareDatetime, ConfigDict
from typing import Annotated
from app.schemas import string_size100
from pydantic import AfterValidator
from datetime import timezone, datetime
from app.models import Cards
import datetime



class Get_exchange_schema(BaseModel):
    collection_name: str | None = None
    is_auction: bool | None = False
    is_favorite: bool | None = False
    id_user_auction: int | None = None
    auction_bet: int | None = 0
    time_limit_auction: datetime.datetime | None = None
    time_created_auction: datetime.datetime | None = None
    time_acquisition: datetime.datetime | None = None
    is_finish_auction: bool | None = False
    is_shiny: bool
    model_config = ConfigDict(from_attributes=True)

class Card_schema(BaseModel):
    id_card:int
    
    atk: float
    def_: float
    value_exchange: int
    covers_urls: list[str]
    description: str | None = None
    urlExtern: list[str] | None = None
    urlIgdb: str | None = None
    name: str
    name_franchise:str | None = None
    game_type:int
    colors: int | None = None
    parent_game_id: int | None = None
    genre:list[str] | None = None
    company_game:list[str] | None = None
    model_config = ConfigDict(from_attributes=True)

    

class Card_user_schema(BaseModel):
    card: Card_schema
    card_user: Get_exchange_schema



 
