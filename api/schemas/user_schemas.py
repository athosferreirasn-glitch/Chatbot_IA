from pydantic import BaseModel, EmailStr, Field
from typing import Any


class UserCreate(BaseModel):
    _uuid = Any
    name: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=32)
    _created_at = Any