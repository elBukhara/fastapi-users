from typing import TYPE_CHECKING, Annotated
from fastapi import Depends

from database import get_async_session
from auth.models.user import UserAuth

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(get_async_session),
    ],
):
    yield UserAuth.get_db(session=session)

