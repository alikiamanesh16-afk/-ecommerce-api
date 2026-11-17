
from scr.repositories.shops import (
    create_shop as create_shop_repository,
    get_shop_by_id,
    get_all_shops,
    update_shop as update_shop_repository
)


def shop_to_dict(shop):
    return {
        "id": shop[0],
        "member_id": shop[1],
        "name": shop[2],
        "introduction": shop[3],
        "category": shop[4]
    }


def create_shop(data):
    shop = create_shop_repository(
        data.member_id,
        data.name,
        data.introduction,
        data.category
    )

    return shop_to_dict(shop)


def get_shop(shop_id):
    shop = get_shop_by_id(shop_id)

    if not shop:
        return None

    return shop_to_dict(shop)


def get_shops():
    shops = get_all_shops()

    return [shop_to_dict(shop) for shop in shops]


def update_shop(shop_id, data):
    shop = update_shop_repository(
        shop_id,
        data.name,
        data.introduction,
        data.category
    )

    if not shop:
        return None

    return shop_to_dict(shop)
