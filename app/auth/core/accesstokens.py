from typing import TYPE_CHECKING, Annotated
from fastapi import Depends

from database import get_async_session
from auth.models.accesstoken import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
    session: Annotated[
        "AsyncSession",
        Depends(get_async_session),
    ],
):  
    yield AccessToken.get_db(session=session)