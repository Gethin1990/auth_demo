import string

from entity.do.base import Base_DO


class Role(Base_DO):
    def __init__(self, name, id=0, is_active=True):
        super().__init__(id, is_active)
        self.name = name
