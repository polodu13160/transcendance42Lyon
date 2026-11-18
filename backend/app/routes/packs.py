
from pydantic import BaseModel, EmailStr, Field, ConfigDict,TypeAdapter,PrivateAttr, ValidationError, model_validator
from typing import Annotated
from fastapi import HTTPException
from app.models import Users
import datetime
from app.auth.auth import mailAuth, nicknameAuth, create_user
from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from app.models.base import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from app.auth.sessions import get_user_from_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# POST /api/v1/auth/login

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = get_user_from_token(token)
    if user == None:
        raise HTTPException()



routerAuth = APIRouter(
    prefix="/packs",
    responses={404: {"page": "Not found"}},
)




@routerAuth.post('/free', description="authentification user")
async def free_pack(current_user: Annotated[Users, Depends(get_current_user)]):
    pass

    







@routerAuth.post('/buy', description="authentification user")
async def buy_pack():
    pass



