from main import app
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.getcwd())


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_create_user():
    response = client.post('/user/',
                           json={
                               "firstname": "string",
                               "lastname": "string",
                               "username": "string",
                               "email": "user@example.com",
                               "password": "string"
                           },)
    assert response.status_code == 200
