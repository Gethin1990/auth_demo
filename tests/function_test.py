import os
import sys

from requests import post
sys.path.append(os.getcwd())

import json

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
    #assert response.text =='true'

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
    #assert response.text =='false'

def test_delete_role_and_relationship_success():
    test_add_user_role_success()
    response = client.delete('/role/1')
    assert response.status_code == 200

def test_authenticate_401():
    response = client.post("/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, data={"username": "test", "password": "test"})
    assert response.status_code == 401

def test_authenticate_success():
    response = client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "test",
                               "email": "user@example.com",
                               "password": "test"
                           },)
    response = client.post("/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, data={"username": "test", "password": "test"})
    
    assert response.status_code == 200
    assert response.text!=''
def test_authenticate_failed():
    response = client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "test",
                               "email": "user@example.com",
                               "password": "test"
                           },)
    response = client.post("/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, data={"username": "test111", "password": "test111"})
    
    assert response.status_code == 401



def test_invalidate():
    print()

def test_delete_user():
    # token =get_token()
    # response = client.delete('/user/1',headers={'Authorization':'Bearer '+token})
    print()

def test_check_role():
    # token =get_token()
    # response = client.post('/role/check_role',headers={'Authorization':'Bearer '+token},json={"name":"role1"})
    # assert response.status_code==200

    print()

def test_all_roles():
    # token =get_token()
    # response = client.get('/role',headers={'Authorization':'Bearer '+token})
    # assert response.status_code==200
    print()
    



def get_token():
    add_user()
    response = client.post("/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, data={"username": "abc1", "password": "abc1"})
    return response.json()['access_token']
    



def add_user():
    client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc1",
                               "email": "user@example.com",
                               "password": "abc1"
                           },)
    client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc2",
                               "email": "user@example.com",
                               "password": "abc2"
                           },)
    client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc3",
                               "email": "user@example.com",
                               "password": "abc3"
                           },)
    client.post('/user/',
                           json={
                               "firstname": "firstname",
                               "lastname": "lastname",
                               "username": "abc4",
                               "email": "user@example.com",
                               "password": "abc4"
                           },)

def add_role():
    client.post('/role/',json={"name":"role1"})
    client.post('/role/',json={"name":"role2"})
    client.post('/role/',json={"name":"role3"})
    client.post('/role/',json={"name":"role4"})
def add_user_role():
    client.put('/role/add_user_role/',json={ "user_id": 1, "role_id": 1},)
    client.put('/role/add_user_role/',json={ "user_id": 1, "role_id": 2},)
    client.put('/role/add_user_role/',json={ "user_id": 1, "role_id": 3},)
    client.put('/role/add_user_role/',json={ "user_id": 2, "role_id": 2},)
    client.put('/role/add_user_role/',json={ "user_id": 2, "role_id": 3},)