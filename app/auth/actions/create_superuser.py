import asyncio
import contextlib

from fastapi_users.exceptions import UserAlreadyExists

from database import async_session
from auth.models.user import UserAuth
from auth.core.users import get_users_db
from auth.core.user_manager import get_user_manager
from auth.schemas.user import UserCreate
from auth.authentication.user_manager import UserManager


get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

# TODO: store in .env files
default_email = "admin@admin.com"
default_username = "superuser"
default_password = "admin"
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> UserAuth:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
        
    )
    
    return user

async def create_superuser(
    email: str = default_email,
    username: str = default_username,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        email = email,
        username = username,
        password = password,
        is_active = is_active,
        is_superuser = is_superuser,
        is_verified = is_verified
    )
    
    try:
        async with async_session() as session:
            async with get_users_db_context(session) as users_db:
                async with get_user_manager_context(users_db) as user_manager:
                    
                    return await create_user(
                        user_manager=user_manager,
                        user_create=user_create,
                    )
                    
    except UserAlreadyExists:
        print(f"User {email} already exists")        


if __name__ == "__main__":
    asyncio.run(create_superuser())

"""
To create a new superuser, go to main.py and include in lifespan(app: FastAPI):

from auth.actions.create_superuser import create_superuser
 
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_superuser()
    ...

"""