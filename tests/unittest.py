from hashlib import new
from infrastructure.operation.user import User,user_op
from infrastructure.status_code.status_code_enum import StatusCodeEnum


def test_user_add():
    user = User('username','firstname','lastname','email','hashed_password')
    r = user_op.create(user)
    assert r ==1


def test_user_add_2():
    user_op.clear()
    user = User('username','firstname','lastname','email','hashed_password')
    user_op.create(user)

    user = User('username1','firstname','lastname','email','hashed_password')
    r =user_op.create(user)
    assert r!=0

def test_user_get_all():
    test_user_add_2()
    r =user_op.get_all()
    assert len(r)==2

def test_user_get_id():
    test_user_add_2()
    r =user_op.get(1)
    assert r.username=='username' 



def test_user_get_by_username():
    test_user_add_2()
    r =user_op.get_by_username('username')
    assert r.username=='username' 


def test_user_get_by_username_2():
    test_user_add_2()
    r =user_op.get_by_username('user1')
    assert r==None


def test_user_get_no_id():
    test_user_add_2()
    r =user_op.get(3)
    assert r ==None

def test_user_update_firstname():
    test_user_add_2()
    user =user_op.get(1)
    user.firstname = 'firstname2'
    r =user_op.update(user)

    assert r.firstname == 'firstname2'

def test_user_delete():
    test_user_add_2()
    user =user_op.get(1)
    user_op.delete(1)
    r = user_op.get(1)

    assert r==None


    
