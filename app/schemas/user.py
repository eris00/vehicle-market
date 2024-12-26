from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str


class UserCreate(UserBase):
    password: str

class UserRegister(UserBase):
    password: str
    is_active: int = True


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    is_active: bool = True
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel): 
    username: str | None = None