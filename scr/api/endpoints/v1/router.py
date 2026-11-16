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