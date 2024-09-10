from fastapi import APIRouter

from auth.core.fastapi_users import fastapi_users
from auth.schemas.user import UserRead, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate
    ),
)