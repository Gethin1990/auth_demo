# Auth Demo For Python

This Demo is use fastapi to build the solution of authoritarian and authenticate.
This Demo is build by VS Code. The project is build form 0 to 1 for python exercise. The Demo is only for interview building, Base I have not builded API by python, it is the fist time for me to build the demo, it is simple and still have many improvements.

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
pip install pytest
```

- download the code

- click the debug icon and select 'fastapi'

- open the url as below, and it will show the Open API document

<http://127.0.0.1:8000/docs>

or

quick start the service

`uvicorn main:app --reload`

## The Test Screenshot

The Test Screenshot in the folder 'api_test_screenshot'

## Code framework document

The code include 4 layers as below.

### API

api: API layer is used to provide the service for client.

api provide the function as below:

auth: get token, and renew token.

user: crate user, delete user.

role: add role, delete role, add use role, get role,check role.

### entity

entity: Entity layer include dto and do model. DTO is date transfer object,it is used for API transfer model include request and response. DO is domain object, it is defined for the domain model.

### infrastructure

infrastructure: Infrastructure layer will provide the based infrastructure capacity for the whole solution, like Cache, Storage,Operation, Internal Status Code.

This layer include 3 parts: Operation, Storage and Status Code.

Storage use singleton patten for saving the data in to memory.And think about the function for integration SQL or No-SQL in the future, I design it as table name-id-value patten to save the date. And the Cache is designed 2 hours expired for save the token as black list to make sure the token could used only once.

Operation is used for operate the data, they inherit by based operate and easy to use with strategy and factory patten.

Status Code is used for mark the operate status.

### Settings

The setting config as below.

```text
environment: Environment = "development"
token_generator_secret_key: str = secrets.token_hex(64)
access_token_expire_minutes: int = 120
refresh_token_expire_minutes: int = 120
api_disable_docs: bool = False
api_debug: bool = True
```

### Test

test: Test layer is for unit test. We use pytest framework for UT. The unit test include Function Test, Unit Test, Storage Test parts.

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
