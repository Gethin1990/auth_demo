import string

from model.role import Role


class User(object):
    id:int
    is_active:bool
    username:string
    firstname:string
    lastname:string
    email:string
    hashed_password:string
    roles: list[Role]