from fastapi_users import FastAPIUsers
from auth.models.user import UserAuth

from auth.types.user_id import UserIdType
from .user_manager import get_user_manager
from .backend import authentication_backend


fastapi_users = FastAPIUsers[UserAuth, UserIdType](
    get_user_manager,
    [authentication_backend],
)