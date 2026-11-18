
from pydantic import BaseModel, EmailStr, Field, ConfigDict,TypeAdapter,PrivateAttr, ValidationError, model_validator
from typing import Annotated
from fastapi import HTTPException
from app.models import Users
import datetime
from app.auth.auth import mailAuth, nicknameAuth, create_user
from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError
from app.models.base import SessionLocal





# POST /api/v1/auth/login


routerAuth = APIRouter(
    prefix="/auth",
    responses={404: {"page": "Not found"}},
)






Email_validator = TypeAdapter(EmailStr)
Identifier= Annotated[str, Field(min_length=3, description="Email or nickname")]
Password= Annotated[str ,Field(min_length=3, description="password")]



class UserAuth(BaseModel):
    identifier: Identifier
    password: Password
    _is_email: bool =  PrivateAttr(default=False)

    @model_validator(mode="after")
    def check_identifier_type(self) -> "UserAuth":
        try:
          Email_validator.validate_python(self.identifier)
          self._is_email = True
        except ValidationError:
          self._is_email = False
        return self


class UserPost(BaseModel):
    id_user:int
    last_name:str
    first_name:str
    nick_name: str
    date_created:datetime.datetime
    id_wallet: int | None  
    date_free_pack: datetime.datetime
    user_email: str
    model_config = ConfigDict(from_attributes=True)

class UserRegister(BaseModel):
    last_name:str
    first_name:str
    nick_name: str
    id_wallet: int | None = None  
    user_email: EmailStr
    password: Password







@routerAuth.post('/login', description="authentification user")
async def login(body: UserAuth):
    try :
        if body._is_email == True:
            user, token = mailAuth(body.identifier, body.password)
        else:
            user, token = nicknameAuth(body.identifier, body.password)
    except:
        raise HTTPException(status_code=401, detail="nickname/mail or password error")
    return {"user": UserPost.model_validate(user), "token": token}

@routerAuth.post('/register', description="register user")
async def register(body: UserRegister ):
    with SessionLocal() as db:
        try:
            user, token = create_user(db, body.first_name, body.last_name, body.nick_name, body.user_email, body.password, body.id_wallet)
        except IntegrityError as i:
            # pos = 
            if (i.args[0].find('user_email') != -1):
                msg = "Email error"
            elif (i.args[0].find('nick_name') != -1):
                msg = "Nickname error"
            else:
                msg = "Error"


            raise HTTPException(
                status_code=409,
                detail=msg)
        return {"user": UserPost.model_validate(user), "token": token}
        





    

        



