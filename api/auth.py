from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError
from infrastructure.operation.user import user_op

from infrastructure.operation.auth import authenticate_user,create_access_token
from entity.dto.token import Token,TokenData
from entity.dto.renew import RenewToken
from settings import Settings,get_settings

router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "not found"}},
)



@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 config: Settings = Depends(get_settings)):
    user = authenticate_user(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=get_settings().access_token_expire_minutes)
    refresh_token_expires = timedelta(minutes=get_settings().refresh_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    refresh_token = create_access_token(
        data={"sub": user.username}, expires_delta=refresh_token_expires
    )
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/refresh", response_model=Token)
async def refresh(renewtoken: RenewToken, config: Settings = Depends(get_settings)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate refresh token",
        headers={"www-Authenticate": "Bearer"},
    )
    try:
        playload = jwt.decode(renewtoken.refresh_token, config.token_generator_secret_key, algorithms=["HS256"])
        username: str = playload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = user_op.get_by_username(token_data.username)
    if user is None or not user.is_active:
        raise credentials_exception
    access_token_expires = timedelta(minutes=get_settings().access_token_expire_minutes)
    refresh_token_expires = timedelta(minutes=get_settings().refresh_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    refresh_token = create_access_token(
        data={"sub": user.username}, expires_delta=refresh_token_expires
    )
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}