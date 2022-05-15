
from typing import List
import json
from fastapi import APIRouter, Depends, HTTPException
from entity.do.user import User

from infrastructure.operation.auth import get_password_hash, get_current_user

from infrastructure.operation.user import user_op
from infrastructure.operation.role import role_user_op

from entity.dto.user import UserOut,UserCreate
from infrastructure.status_code.status_code_enum import StatusCodeEnum
router = APIRouter(prefix="/user", tags=["User"])

# @router.get("/", response_model=List[UserResponse])
# async def read_users():
#     res =user_op.get_all()
#     return res


@router.post("/", response_model=int)
async def create_user(user_request:UserCreate):
    user = user_op.get_by_username(user_request.username)
    if  user:
         raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system",
        )
    
    user = User(user_request.username,
    user_request.firstname,
    user_request.lastname,
    user_request.email,
    hashed_password=get_password_hash(user_request.password),
    )
    
    id = user_op.create(user)
    return id
    

@router.delete("/{user_id}/", status_code=204)
async def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_user)):
    user =user_op.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.id == user_id:
        raise HTTPException(status_code=403, detail="User can't delete itself")

    
    relationship = role_user_op.get_role_by_userid(0,user_id)
    if relationship:
        for item in relationship:
            role_user_op.delete(item.id)
    user_op.delete(user_id)