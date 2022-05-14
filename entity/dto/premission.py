from typing import List

from pydantic import BaseModel

from entity.dto.role import Role

class PermissionBase(BaseModel):
    name: str
class Permission(PermissionBase):
    id: int
    roles: List[Role] = []