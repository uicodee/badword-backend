from fastapi import APIRouter, Depends

from app import dto
from app.api.dependencies import get_user

router = APIRouter(prefix="/user")


@router.get(
    path="/get-me",
    description="Get a user's information",
    summary="Get current user's information",
    response_model=dto.User,
)
async def get_me(user: dto.User = Depends(get_user)) -> dto.User:
    return user
