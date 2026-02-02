from pydantic import BaseModel, Field
from pydantic import ConfigDict


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    author: str = Field(min_length=1, max_length=255)
    isbn: str = Field(min_length=10, max_length=13)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=255)
    author: str | None = Field(default=None, max_length=255)


class BookRead(BookBase):
    id: int
    owner_id: int | None

    model_config = ConfigDict(from_attributes=True)
