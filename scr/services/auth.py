
from pwdlib import PasswordHash

from scr.repositories.members import (
    create_member,
    get_member_by_phone,
    get_member_by_username
)

password_hasher = PasswordHash.recommended()


def register_member(data):
    if get_member_by_phone(data.phone_number):
        raise ValueError("Phone number already exists")

    if get_member_by_username(data.username):
        raise ValueError("Username already exists")

    hashed_password = password_hasher.hash(data.password)

    member = create_member(
        data.name,
        data.phone_number,
        data.username,
        hashed_password
    )

    return {
        "id": member[0],
        "name": member[1],
        "phone_number": member[2],
        "username": member[3]
    }
