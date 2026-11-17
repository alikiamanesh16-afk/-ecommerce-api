
from scr.repositories.products import (
    create_product as create_product_repository,
    get_products_by_shop,
    get_product_by_id as get_product_by_id_repository,
    update_product as update_product_repository,
    delete_product as delete_product_repository
)

from scr.repositories.shops import get_shop_by_id


def product_to_dict(product):
    return {
        "id": product[0],
        "shop_id": product[1],
        "name": product[2],
        "description": product[3],
        "stock": product[4],
        "price": product[5],
        "is_active": product[6]
    }


def create_product(shop_id, data):
    if not get_shop_by_id(shop_id):
        raise ValueError("Shop not found")

    product = create_product_repository(
        shop_id,
        data.name,
        data.description,
        data.stock,
        data.price,
        data.is_active
    )

    return product_to_dict(product)


def get_products(shop_id):
    if not get_shop_by_id(shop_id):
        raise ValueError("Shop not found")

    products = get_products_by_shop(shop_id)

    return [product_to_dict(product) for product in products]


def get_product(product_id):
    product = get_product_by_id_repository(product_id)

    if not product:
        return None

    return product_to_dict(product)


def update_product(product_id, data):
    product = update_product_repository(
        product_id,
        data.name,
        data.description,
        data.stock,
        data.price,
        data.is_active
    )

    if not product:
        return None

    return product_to_dict(product)


def delete_product(product_id):
    return delete_product_repository(product_id)
