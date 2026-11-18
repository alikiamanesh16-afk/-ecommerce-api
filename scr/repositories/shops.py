
from scr.connections.postgresql import get_connection


def create_shop(member_id, name, introduction, category):
    with get_connection() as conn:
        shop = conn.execute(
            """
            INSERT INTO shops (member_id, name, introduction, category)
            VALUES (%s, %s, %s, %s)
            RETURNING id, member_id, name, introduction, category
            """,
            (member_id, name, introduction, category)
        ).fetchone()

    return shop


def get_shop_by_id(shop_id):
    with get_connection() as conn:
        shop = conn.execute(
            """
            SELECT id, member_id, name, introduction, category
            FROM shops
            WHERE id = %s
            """,
            (shop_id,)
        ).fetchone()

    return shop


def get_all_shops():
    with get_connection() as conn:
        shops = conn.execute(
            """
            SELECT id, member_id, name, introduction, category
            FROM shops
            ORDER BY id
            """
        ).fetchall()

    return shops


def update_shop(shop_id, name, introduction, category):
    with get_connection() as conn:
        shop = conn.execute(
            """
            UPDATE shops
            SET name = %s,
                introduction = %s,
                category = %s,
                updated_at = NOW()
            WHERE id = %s
            RETURNING id, member_id, name, introduction, category
            """,
            (name, introduction, category, shop_id)
        ).fetchone()

    return shop
