from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class User(UserBase):
    id: int
    username: str
    email: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        orm_mode = True