from pydantic import BaseModel, AwareDatetime
from typing import Annotated
from app.schemas import string_size100
from pydantic import AfterValidator
from datetime import timezone, datetime


def setTimeTimezone0(value: AwareDatetime):
    return value.astimezone(timezone.utc)
    

class User_schema(BaseModel):
    id_user: int
    last_name: string_size100
    first_name: string_size100
    nick_name: string_size100
    date_created: Annotated[AwareDatetime, AfterValidator(setTimeTimezone0)]
    id_wallet: int
    amount_crypto: float
    date_free_pack: datetime


