
from scr.connections.postgresql import get_connection


def create_member(name, phone_number, username, password_hash):
    with get_connection() as conn:
        member = conn.execute(
            """
            INSERT INTO members (name, phone_number, username, password_hash)
            VALUES (%s, %s, %s, %s)
            RETURNING id, name, phone_number, username
            """,
            (name, phone_number, username, password_hash)
        ).fetchone()

    return member


def get_member_by_phone(phone_number):
    with get_connection() as conn:
        member = conn.execute(
            "SELECT * FROM members WHERE phone_number = %s",
            (phone_number,)
        ).fetchone()

    return member


def get_member_by_username(username):
    with get_connection() as conn:
        member = conn.execute(
            "SELECT * FROM members WHERE username = %s",
            (username,)
        ).fetchone()

    return member