from fastapi import FastAPI
from .authentication import router as authentication_router
from .word import router as word_router
from .user import router as user_router


def setup(app: FastAPI) -> None:
    app.include_router(router=authentication_router, tags=["Authentication"])
    app.include_router(router=word_router, tags=["Word"])
    app.include_router(router=user_router, tags=["User"])
