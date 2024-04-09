from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm

from app import dto
from app.api import schems
from app.api.dependencies import dao_provider, AuthProvider, get_settings
from app.config import Settings
from app.infrastructure.database.dao.holder import HolderDao

router = APIRouter()


@router.post(
    path="/login",
    description="Login user",
    summary="Login user by email and password",
    response_model=dto.Token,
)
async def login_user(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    dao: HolderDao = Depends(dao_provider),
    settings: Settings = Depends(get_settings),
) -> dto.Token:
    auth = AuthProvider(settings=settings)
    user = await auth.authenticate_user(form_data.username, form_data.password, dao)
    token = auth.create_user_token(user=user)
    response.set_cookie(key="accessToken", value=token.access_token, httponly=True)
    return token
