from fastapi import APIRouter

from Endpoints import auth, chat

router  = APIRouter()

router.include_router(
    auth.router,
    prefix="/auth",
)

router.include_router(
    chat.router,
    prefix="/chat"
)
