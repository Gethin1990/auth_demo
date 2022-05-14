from enum import Enum


class StatusCodeEnum(Enum):

    OK = (0, 'success')
    ERROR = (-1, 'error')
    SERVER_ERROR = (500, 'internal error')
    STORAGE_ERROR = (5000, 'storage error')
    STORAGE_NO_TABLE_NAME = (5001, 'storage error')
    STORAGE_NOT_FOUND = (5002, 'not found in storage')

    @property
    def code(self):
        """获取状态码"""
        return self.value[0]

    @property
    def errmsg(self):
        """获取状态码信息"""
        return self.value[1]