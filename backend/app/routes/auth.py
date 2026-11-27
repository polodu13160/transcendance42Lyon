
from pydantic import BaseModel, EmailStr, Field, ConfigDict,TypeAdapter,PrivateAttr, ValidationError, model_validator
from typing import Annotated
from fastapi import HTTPException, status
from app.models import Users
import datetime
from app.auth.auth import mailAuth, nicknameAuth, create_user
from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from app.models.base import SessionLocal
from app.schemas.Error import HttpErrorSchema
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth.sessions import get_user_from_token
from sqlalchemy.orm import Session
from app.models.base import get_db
from argon2.exceptions import VerifyMismatchError





# POST /api/v1/auth/login


routerAuth = APIRouter(
    prefix="/auth"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(get_db)]):

    current_user = get_user_from_token(token, db)
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user








Email_validator = TypeAdapter(EmailStr)
Identifier= Annotated[str, Field(min_length=3, description="Email or nickname")]
Password= Annotated[str ,Field(min_length=3, description="password")]
no = Annotated[str, Field(pattern=r"^[^@]*$")]



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
    nick_name: Annotated[str, Field(min_length=3, description="Email or nickname")]
    id_wallet: int | None = None  
    user_email: EmailStr
    password: Password



@routerAuth.get('verif-token', description="""verif token is good
**Header required:**
`Authorization: Bearer <TOKENSHASH>`"""
)
async def verif(current_user: Annotated[Users, Depends(get_current_user)]):
    return {"message": "user connected", "user": UserPost.model_validate(current_user)}




@routerAuth.post('/login')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db)]):
    try:
              Email_validator.validate_python(form_data.username)
              is_email = True
    except ValidationError:
              is_email = False
    try :
        if is_email == True:
            user, token = mailAuth(form_data.username, form_data.password, db)
        else:
            
            user, token = nicknameAuth(form_data.username, form_data.password, db)
    except VerifyMismatchError:
        raise HTTPException(status_code=401, detail="nickname/mail or password error")
    return {"user": UserPost.model_validate(user), "access_token": token, "token_type": "bearer"}

@routerAuth.post('/register', description="""
> [WARNING]\n
> ne pas mettre le meme nickname, mail ou id wallet,
ps **je temmerde kais** """)
async def register(body: UserRegister, db: Annotated[Session, Depends(get_db)] ):
   
    try:
        user, token = create_user(db, body.first_name, body.last_name, body.nick_name, body.user_email, body.password, body.id_wallet)
    except IntegrityError as i:
        error_msg = str(i.orig).lower()
        print("DEBUG INTEGRITY ERROR:", error_msg)
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
    return {"user": UserPost.model_validate(user), "access_token": token, "token_type": "bearer"}


        
# @routerAuth.get('/token-api', description="for use api public, not access change password or sensibility data")
# async def create_token(user_nickname: str, password: str):
#     var = login()





    

        



