from typing import Annotated
from fastapi import APIRouter, Depends

from auth.models.user import UserAuth
from auth.core.fastapi_users import current_user, current_superuser
from auth.schemas.user import UserRead

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
)

@router.get("/current_user")
def get_user_messages(
    user: Annotated[
        UserAuth,
        Depends(current_user)
    ],
):
    return {
        "messages": ["Hello, World!", "The message for current user."],
        "user": UserRead.model_validate(user)
    }

@router.get("/super_user")
def get_superuser_messages(
    supreruser: Annotated[
        UserAuth,
        Depends(current_superuser)
    ],
):
    return {
        "messages": ["Hello, FastAPI!", "The message for superuser."],
        "superuser": UserRead.model_validate(supreruser)
    }