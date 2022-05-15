
from operator import mod
from statistics import mode
import string
from tkinter.tix import Tree
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from infrastructure.operation.storage import Storage
from entity.do.base import Base_DO
from infrastructure.status_code.status_code_enum import StatusCodeEnum
ModelType = TypeVar("ModelType")


class Base(Generic[ModelType]):
    def __init__(self, table_name: string, model: Generic[ModelType]) -> None:
        self._model = model
        self.storage = Storage()
        self.table_name = table_name

    def create(self, model) -> int:
        if not model.id or model.id == 0:
            res = self.storage.get(self.table_name)
            if isinstance(res, StatusCodeEnum) and res == StatusCodeEnum.STORAGE_NO_TABLE_NAME:
                model.id = 1
            else:
                model.id = len(res)+1

        self.storage.set(self.table_name, model.id, model)
        return model.id

    def get_all(self) -> List[ModelType]:
        users = self.storage.get(self.table_name)
        return list(filter(lambda x: x.is_active, users))

    def get(self, id) -> ModelType:
        return self.storage.get(self.table_name, id)

    def update(self, model) -> ModelType:
        if not model.id or model.id == 0:
            return None
        self.storage.set(self.table_name, model.id, model)
        return model

    def delete(self, id) -> ModelType:
        model = self.get(id)
        if not model:
            return None
        model.is_active = False
        self.storage.set(self.table_name, model.id, model)
        return model

    def get_by_username(self, user_name) -> ModelType:
        if self.table_name != 'User':
            return StatusCodeEnum.STORAGE_NO_TABLE_NAME
        users = self.storage.get(self.table_name)
        if isinstance(users, StatusCodeEnum):
            return None

        user = list(filter(lambda x: x.username == user_name, users))
        if not user or len(user) == 0:
            return None
        else:
            return user[0]

    def get_by_rolename(self, role_name) -> ModelType:
        if self.table_name != 'Role':
            return StatusCodeEnum.STORAGE_NO_TABLE_NAME
        roles = self.storage.get(self.table_name)
        if isinstance(roles, StatusCodeEnum):
            return None

        role = list(filter(lambda x: x.name == role_name, roles))
        if not role or len(role) == 0:
            return None
        else:
            return role[0]

    def get_role_by_userid(self, rid=0, uid=0):
        if self.table_name != 'User_Role':
            return StatusCodeEnum.STORAGE_NO_TABLE_NAME
        tb = self.storage.get(self.table_name)
        if isinstance(tb, StatusCodeEnum):
            return None
        res = None
        if rid == 0:
            res = list(filter(lambda x: x.user_id == uid, tb))
        elif uid == 0:
            res = list(filter(lambda x: x.role_id == rid, tb))
        else:
            res = list(filter(lambda x: x.role_id ==
                       rid and x.user_id == uid, tb))
        return res

    def clear(self):
        self.storage.clear()
