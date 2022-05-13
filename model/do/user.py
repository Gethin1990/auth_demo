
import string
from typing import List

from model.do.role import Role


class User(object):
    id:int
    is_active:bool
    username:string
    firstname:string
    lastname:string
    email:string
    hashed_password:string
    roles: List[Role]