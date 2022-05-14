from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass
class RoleCheck(RoleBase):
    pass


class RoleUpdate(RoleBase):
    user_id:str
    role_id:str


class RoleResponse(RoleBase):
    id: int
