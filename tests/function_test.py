import os
import sys
sys.path.append(os.getcwd())

from main import app
from fastapi.testclient import TestClient



client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

# no auth
def test_create_user_success():
    response = client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc",
                               "email": "user@example.com",
                               "password": "password"
                           },)
    assert response.status_code == 200
    assert response.text =='1'

def test_create_user_fail():
    response = client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc",
                               "email": "user@example.com",
                               "password": "password"
                           },)
    response = client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc",
                               "email": "user@example.com",
                               "password": "password"
                           },)
    assert response.status_code == 409



def test_create_role_success():
    response = client.post('/role/',
                           json={
                               "name":"role"
                           },)
    assert response.status_code == 200
    assert response.text =='1'

def test_create_role_failed():
    response = client.post('/role/',
                           json={
                               "name":"role"
                           },)
    response = client.post('/role/',
                           json={
                               "name":"role"
                           },)
    assert response.status_code == 404

def test_delete_role_success():
    response = client.post('/role/',
                           json={
                               "name":"role1"
                           },)
    response = client.post('/role/',
                           json={
                               "name":"role2"
                           },)
    response = client.delete('/role/1')
    assert response.status_code == 200

def test_delete_role_and_relationship_success():
    test_add_user_role_success()
    response = client.delete('/role/1')
    assert response.status_code == 200

def test_delete_role_failed():
    response = client.post('/role/',
                           json={
                               "name":"role1"
                           },)
    response = client.post('/role/',
                           json={
                               "name":"role2"
                           },)
    response = client.delete('/role/3')
    assert response.status_code == 404
    

def test_add_user_role_success():
    response = client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc",
                               "email": "user@example.com",
                               "password": "password"
                           },)
    response = client.post('/role/',
                           json={
                               "name":"role1"
                           },)
    response = client.put('/role/add_user_role/',
                            json={
                                "user_id": 1,
                                "role_id": 1
                            },)
                    
    assert response.status_code == 200
    assert response.text =='true'

def test_add_user_role_failed():
    response = client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc",
                               "email": "user@example.com",
                               "password": "password"
                           },)
    response = client.post('/role/',
                           json={
                               "name":"role1"
                           },)
    response = client.put('/role/add_user_role/',
                            json={
                                "user_id": 1,
                                "role_id": 2
                            },)
                    
    assert response.status_code == 200
    assert response.text =='false'


def test_authenticate():
    
    print()

def test_invalidate():
    print()

def test_delete_user():
    response = client.delete('/user/1')
    print()

def test_check_role():
    print()

def test_all_roles():
    print()



def test_get_token():
    
    form_data = 'grant_type=&username=abc&password=abc&scope=&client_id=&client_secret='
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json'
    }
    response = client.post('/token/', data=form_data, headers=headers)
    assert response.status_code == 200

