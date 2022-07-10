from typing import Optional
from pydantic import BaseModel, EmailStr

from app.models.user import UserType


class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserCreate(UserBase):
    password: str
    user_type: UserType


class UserSignin(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: int
    password: Optional[str] = None

    class Config:
        orm_mode = True


class UserRead(UserInDBBase):
    pass
