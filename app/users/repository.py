from database import async_session

from .models import UserOrm
from .schemas import User

class UserRepository:
    @classmethod
    async def get_user(cls, user_id: int) -> User:
        async with async_session() as session:
            user = await session.get(UserOrm, user_id)
            return user