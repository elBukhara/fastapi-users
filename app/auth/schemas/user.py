from fastapi_users import schemas

from auth.types.user_id import UserIdType

class UserRead(schemas.BaseUser[UserIdType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    pass