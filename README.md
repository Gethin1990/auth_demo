# Auth Demo For Python

This Demo is use fastapi to build the solution of authoritarian and authenticate.
This Demo is build by VS Code. The project is build form 0 to 1 for python exercise.

## How to build and debug the code

The code build steps:

- install the dependency package as below

```shell
pip install fastapi
pip install "uvicorn[standard]"
pip install fastapi-jwt-auth
pip install pydantic[email]
pip install python-jose
pip install passlib
pip install bcrypt
pip install python-multipart
```

- download the code

- click the debug icon and select 'fastapi'

- open the url as below, and it will show the Open API document

<http://127.0.0.1:8000/docs>

or

quick start the service

`uvicorn main:app --reload`

## Technology Points

1. User password encryption by 'bcrypt'.
2. As the AC remind ,the token could only use for 1 time, you should renew token pre-request
3. Cache
4. Storage
5. FastAPI
6. Status Code
7. OAuth and JWT

## TODO LIST

### Infrastructure

- [x] Find API Framework
- [x] Build UT
- [x] Build Model
- [x] Build Storage
- [x] Readme.md
- [ ] UT for function

### Functions

- [x] Create User
- [x] Delete User
- [x] Create Role
- [x] Delete Role
- [x] Add Role to User
- [x] Authenticate
- [x] Invalidate
- [x] Check Role
- [x] All Roles

### Functions in the further

- [ ] Docker and K8S
- [ ] RBAC
