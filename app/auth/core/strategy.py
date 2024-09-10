from typing import TYPE_CHECKING, Annotated
from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy, AccessTokenDatabase

from auth.models.accesstoken import AccessToken
from .accesstokens import get_access_tokens_db

if TYPE_CHECKING:
        from auth.models.accesstoken import AccessToken

def get_database_strategy(
    access_tokens_db: Annotated[
            AccessTokenDatabase[AccessToken],
            Depends(get_access_tokens_db),
        ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_tokens_db, 
        lifetime_seconds=3600
    )