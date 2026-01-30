from pydantic import BaseModel, EmailStr, Field
from pydantic import ConfigDict


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)


class UserRead(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
