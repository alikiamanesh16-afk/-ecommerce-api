from fastapi import APIRouter, HTTPException
from scr.schemas.auth import (
    RegisterRequest,
    RegisterResponse,
    LoginRequest,
    LoginResponse
)

from scr.services.auth import register_member, login_member

from scr.schemas.auth import RegisterRequest, RegisterResponse
from scr.services.auth import register_member

from scr.schemas.shops import ShopCreate, ShopUpdate, ShopResponse
from scr.services.shops import (
    create_shop,
    update_shop,
    delete_shop
)


from scr.schemas.shops import ShopCreate, ShopUpdate, ShopResponse

from scr.services.shops import (
    create_shop,
    get_shop,
    get_shops,
    update_shop
)


from scr.schemas.products import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from scr.services.products import (
    create_product,
    get_products,
    get_product,
    update_product,
    delete_product
)


router = APIRouter()


@router.post("/auth/register", response_model=RegisterResponse)
def register(data: RegisterRequest):
    try:
        return register_member(data)
    except ValueError as error:
        raise HTTPException(
            status_code=409,
            detail=str(error)
        )

@router.post("/auth/login", response_model=LoginResponse)
def login(data: LoginRequest):
    try:
        return login_member(data)
    except ValueError as error:
        raise HTTPException(
            status_code=401,
            detail=str(error)
        )


@router.post("/shops", response_model=ShopResponse, status_code=201)
def create_shop_endpoint(data: ShopCreate):
    return create_shop(data)


@router.get("/shops", response_model=list[ShopResponse])
def get_shops_endpoint():
    return get_shops()


@router.get("/shops/{shop_id}", response_model=ShopResponse)
def get_shop_endpoint(shop_id: int):
    shop = get_shop(shop_id)

    if not shop:
        raise HTTPException(
            status_code=404,
            detail="Shop not found"
        )

    return shop


@router.put("/shops/{shop_id}", response_model=ShopResponse)
def update_shop_endpoint(shop_id: int, data: ShopUpdate):
    shop = update_shop(shop_id, data)

    if not shop:
        raise HTTPException(
            status_code=404,
            detail="Shop not found"
        )

    return shop


@router.post(
    "/shops/{shop_id}/products",
    response_model=ProductResponse,
    status_code=201
)
def create_product_endpoint(shop_id: int, data: ProductCreate):
    try:
        return create_product(shop_id, data)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.get(
    "/shops/{shop_id}/products",
    response_model=list[ProductResponse]
)
def get_products_endpoint(shop_id: int):
    try:
        return get_products(shop_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product_endpoint(product_id: int):
    product = get_product(product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.put(
    "/products/{product_id}",
    response_model=ProductResponse
)
def update_product_endpoint(product_id: int, data: ProductUpdate):
    product = update_product(product_id, data)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.delete(
    "/products/{product_id}",
    status_code=204
)
def delete_product_endpoint(product_id: int):
    product = delete_product(product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return None

