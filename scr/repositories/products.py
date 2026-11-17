
from scr.connections.postgresql import get_connection


def create_product(shop_id, name, description, stock, price, is_active):
    with get_connection() as conn:
        product = conn.execute(
            """
            INSERT INTO products
            (shop_id, name, description, stock, price, is_active)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, shop_id, name, description, stock, price, is_active
            """,
            (shop_id, name, description, stock, price, is_active)
        ).fetchone()

    return product


def get_products_by_shop(shop_id):
    with get_connection() as conn:
        products = conn.execute(
            """
            SELECT id, shop_id, name, description, stock, price, is_active
            FROM products
            WHERE shop_id = %s
            ORDER BY id
            """
        , (shop_id,)).fetchall()

    return products


def get_product_by_id(product_id):
    with get_connection() as conn:
        product = conn.execute(
            """
            SELECT id, shop_id, name, description, stock, price, is_active
            FROM products
            WHERE id = %s
            """,
            (product_id,)
        ).fetchone()

    return product


def update_product(product_id, name, description, stock, price, is_active):
    with get_connection() as conn:
        product = conn.execute(
            """
            UPDATE products
            SET name = %s,
                description = %s,
                stock = %s,
                price = %s,
                is_active = %s,
                updated_at = NOW()
            WHERE id = %s
            RETURNING id, shop_id, name, description, stock, price, is_active
            """,
            (name, description, stock, price, is_active, product_id)
        ).fetchone()

    return product


def delete_product(product_id):
    with get_connection() as conn:
        product = conn.execute(
            """
            DELETE FROM products
            WHERE id = %s
            RETURNING id
            """,
            (product_id,)
        ).fetchone()

    return product
