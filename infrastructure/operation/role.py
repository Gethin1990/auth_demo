from entity.do.role import Role
from entity.do.user_role import User_Role
from infrastructure.operation.base import Base

role_op = Base("Role",Role)
role_user_op = Base("User_Role",User_Role)