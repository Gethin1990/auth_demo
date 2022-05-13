import string

from model.role import Role

class Permission(object):
    id:int
    name:string
    roles:list[Role]