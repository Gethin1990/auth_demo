from typing import List
from fastapi import status, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from entity.do.user_role import User_Role
from entity.do.role import Role

from infrastructure.operation.role import role_op, role_user_op
from infrastructure.operation.user import user_op
from infrastructure.operation.auth import get_current_user


from entity.dto.role import RoleCheck, RoleCreate, RoleOut, RoleUpdate
from entity.do.role import Role
from entity.do.user import User
from infrastructure.status_code.status_code_enum import StatusCodeEnum

router = APIRouter(
    prefix="/role",
    tags=["role"],
    responses={404: {"description": "not found"}},
)


@router.post("/", response_model=int)
async def post_role(role_request: RoleCreate):
    role_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"role {role_request.name} already exist",
    )
    res = role_op.get_by_rolename(role_request.name)
    if res:
        raise role_exception
    else:
        role = Role(role_request.name)
        id = role_op.create(role)
        return id


@router.delete("/{id_role}", response_model=int)
async def delete_role(id_role: int):
    role_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"could not find role: {id_role}",
    )
    role = role_op.get(id=id_role)

    if role:
        relationship = role_user_op.get_role_by_userid(id_role,0)
        if relationship:
            for item in relationship:
                role_user_op.delete(item.id)
        res = role_op.delete(id_role)
        return res.id
    else:
        raise role_exception


@router.put("/add_user_role/", response_model=bool, status_code=200)
async def add_role_to_user(role_request: RoleUpdate):
    ro_res = role_op.get(role_request.role_id)
    usr_res = user_op.get(role_request.user_id)
    if not ro_res or not usr_res:
        return False
    exist_role = role_user_op.get_role_by_userid(ro_res.id, usr_res.id)
    if exist_role:
        return False

    if ro_res and usr_res:
        ur_model = User_Role(ro_res.id, usr_res.id)
        role_user_op.create(ur_model)
        return True
    return False


@router.post("/check_role/", response_model=bool, status_code=200)
async def check_role(role_request: RoleCheck, current_user: User = Depends(get_current_user)):
    role = role_op.get_by_rolename(role_name=role_request.name)
    exist_role = role_user_op.get_role_by_userid(role.id, current_user.id)
    if isinstance(exist_role, StatusCodeEnum):
        return False

    if len(exist_role) > 0:
        return True
    else:
        return False


@router.get("/", response_model=List[RoleOut], status_code=200)
async def get_roles(current_user: User = Depends(get_current_user)):
    exist_roles = role_user_op.get_role_by_userid(0, current_user.id)
    res =[]
    if exist_roles == None:
        return res
    for ro in exist_roles:
        for role in role_op.get_all():
            if ro.id == role.id:
                res.append({"id":role.id,"name":role.name})
    return res
