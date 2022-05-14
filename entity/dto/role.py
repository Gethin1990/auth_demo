from pydantic import BaseModel


class RoleBase(BaseModel):
    pass


class RoleCreate(RoleBase):
    name: str
    pass
class RoleCheck(RoleBase):
    name: str
    pass


class RoleUpdate(RoleBase):
    user_id:int
    role_id:int


class RoleOut(RoleBase):
    name: str
    id: int
