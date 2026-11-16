from fastapi import APIRouter, HTTPException

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