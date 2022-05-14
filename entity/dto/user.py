from pydantic import BaseModel, EmailStr
class UserBase(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool