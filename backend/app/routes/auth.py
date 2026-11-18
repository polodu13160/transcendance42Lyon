
from pydantic import BaseModel, EmailStr, Field, ConfigDict,TypeAdapter,PrivateAttr, ValidationError, model_validator
from typing import Annotated
from fastapi import HTTPException
from app.models import Users
import datetime
from app.auth.auth import mailAuth, nicknameAuth
from fastapi import APIRouter





# POST /api/v1/auth/login


routerAuth = APIRouter(
    prefix="/auth",
    responses={404: {"page": "Not found"}},
)






email_validator = TypeAdapter(EmailStr)



class UserAuth(BaseModel):
    identifier: EmailStr | str = Field(min_length=3, description="Email or nickname")
    password: str = Field(min_length=3, description="password")
    _is_email: bool =  PrivateAttr(default=False)

    @model_validator(mode="after")
    def check_identifier_type(self) -> "UserAuth":
        try:
          email_validator.validate_python(self.identifier)
          self._is_email = True
        except ValidationError:
          self._is_email = False
        return self


class UserPost(BaseModel):
    id_user: int
    id_user:int
    last_name:str
    first_name:str
    nick_name: str
    date_created:datetime.datetime
    id_wallet: int | None  
    date_free_pack: datetime.datetime
    user_email: str
    model_config = ConfigDict(from_attributes=True)
    





@routerAuth.post('/login', description="authentification user")
async def register(body: UserAuth):
    try :
        if body._is_email == True:
            user, token = mailAuth(body.identifier, body.password)
        else:
            user, token = nicknameAuth(body.identifier, body.password)
    except:
        raise HTTPException(status_code=401, detail="nickname/mail or password error")
    return {"user": UserPost.model_validate(user), "token": token}

    

        



