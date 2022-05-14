
from entity.do.base import Base_DO

class User(Base_DO):
    # username:string
    # firstname:string
    # lastname:string
    # email:string
    # hashed_password:string

    def __init__(self, username,firstname,lastname,email, hashed_password,id = 0,is_active=True):
        super().__init__(id, is_active)
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.hashed_password = hashed_password