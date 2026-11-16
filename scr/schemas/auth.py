
from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    name: str
    phone_number: str = Field(min_length=10, max_length=20)
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)


class RegisterResponse(BaseModel):
    id: int
    name: str
    phone_number: str
    username: str
