import threading

from infrastructure.status_code.status_code_enum import StatusCodeEnum


class Storage(object):
    __STORAGE = dict()
    __instance_lock = threading.Lock()

    def __init__(self):
        self.__storage = Storage.__STORAGE

    def __new__(cls, *args, **kwargs):
        if not hasattr(Storage, "_instance"):
            with Storage.__instance_lock:
                if not hasattr(Storage, "_instance"):
                    Storage._instance = object.__new__(cls)
        return Storage._instance

    def set(self, table_name, id, model):
        if table_name in self.__storage:
            t_store = self.__storage[table_name]
            t_store[id] = model
        else:
            self.__storage[table_name] = {id: model}

    def get(self, table_name, id=-1):
        if not table_name:
            return StatusCodeEnum.STORAGE_ERROR
        if table_name not in self.__storage:
            return StatusCodeEnum.STORAGE_NO_TABLE_NAME
        if id == -1:
            dic = self.__storage[table_name]
            return list(dic.values())
        if id not in self.__storage[table_name]:
            return None
        res = self.__storage[table_name][id]
        if not res:return None
        return res if res.is_active else None

    def delete(self, table_name, key):
        self.__storage[table_name].pop(key)
    def clear(self):
        self.__storage.clear()

