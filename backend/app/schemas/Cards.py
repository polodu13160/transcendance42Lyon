 
from pydantic import BaseModel, AwareDatetime, ConfigDict
from typing import Annotated
from app.schemas import string_size100
from pydantic import AfterValidator
from datetime import timezone, datetime
from app.models import Cards
import datetime



class Get_exchange_schema(BaseModel):
    collection_name: str | None 
    is_auction: bool
    is_favorite: bool
    id_user_auction: int | None
    auction_bet: int
    time_limit_auction: datetime.datetime | None
    time_created_auction:  datetime.datetime | None
    time_acquisition: datetime.datetime
    is_finish_auction: bool
    is_shiny: bool
    model_config = ConfigDict(from_attributes=True)


    

class Card_user_schema(BaseModel):
    card: Cards
    card_user: Get_exchange_schema



 
