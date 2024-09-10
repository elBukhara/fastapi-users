from fastapi import Depends
from fastapi_users import FastAPIUsers, BaseUserManager, IntegerIDMixin

from .models import UserAuth, get_db
from .auth import auth_backend

# Create password hashing logic using bcrypt
SECRET = "SECRET"

class UserManager(IntegerIDMixin, BaseUserManager[UserAuth, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    
    async def on_after_register(self, user: UserAuth, request=None):
        print(f"User {user.username} has registered.")


# Create FastAPI Users instance
async def get_user_manager(user_db = Depends(get_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[UserAuth, int](
    get_user_manager,
    [auth_backend],
)
