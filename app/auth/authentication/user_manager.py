import logging 

from fastapi import Request
from typing import Optional, TYPE_CHECKING
from fastapi_users import BaseUserManager, IntegerIDMixin

from auth.models.user import UserAuth
from auth.types.user_id import UserIdType

if TYPE_CHECKING:
    from fastapi import Request


SECRET = "SECRET"

log = logging.getLogger(__name__)

class UserManager(IntegerIDMixin, BaseUserManager[UserAuth, UserIdType]):
    reset_password_token_secret = '48c30a8c9bdd079166633ae94587a930f301b7137c94760c92421bd5e70e1ee8'
    verification_token_secret = 'b4620e0822ed8cd60f350ca10b01c1a1842f6cd34ffe7bbfc44c21f227a6f478'

    async def on_after_register(
        self,
        user: UserAuth,
        request: Optional["Request"] = None
    ):
        log.warning(
            "User %r has registered.",
            user.id
        )

    async def on_after_request_verify(
        self,
        user: UserAuth,
        token: str, 
        request: Optional["Request"] = None
    ):
        log.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token
        )
    
    async def on_after_forgot_password(
        self,
        user: UserAuth,
        token: str, 
        request: Optional["Request"] = None
    ):
        log.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token
        )