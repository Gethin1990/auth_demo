from infrastructure.operation.storage import Storage
from infrastructure.status_code.status_code_enum import StatusCodeEnum

def test_storage_no_table_find():
    stor = Storage()
    r =stor.get('abc')
    assert isinstance(r,StatusCodeEnum)


def test_storage_no_entity_find():
    stor = Storage()
    stor.set('A',1,None)
    r =stor.get('A',1)
    assert r == None




