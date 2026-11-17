
from decimal import Decimal

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    description: str
    stock: int = Field(ge=0)
    price: Decimal = Field(
        gt=0,
        max_digits=15,
        decimal_places=2
    )
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    description: str
    stock: int = Field(ge=0)
    price: Decimal = Field(
        gt=0,
        max_digits=15,
        decimal_places=2
    )
    is_active: bool


class ProductResponse(BaseModel):
    id: int
    shop_id: int
    name: str
    description: str
    stock: int
    price: Decimal
    is_active: bool
