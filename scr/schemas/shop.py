
from pydantic import BaseModel, Field


class ShopCreate(BaseModel):
    member_id: int
    name: str = Field(min_length=2, max_length=150)
    introduction: str
    category: str = Field(min_length=2, max_length=100)


class ShopUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    introduction: str
    category: str = Field(min_length=2, max_length=100)


class ShopResponse(BaseModel):
    id: int
    member_id: int
    name: str
    introduction: str
    category: str
