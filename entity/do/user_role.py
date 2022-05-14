
from entity.do.base import Base_DO

class User_Role(Base_DO):
    def __init__(self, id, role_id,user_id,is_active=True,):
        super().__init__(id, is_active)
        self.role_id = role_id
        self.user_id = user_id
    