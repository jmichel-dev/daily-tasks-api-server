from fastapi import APIRouter

from daily_tasks_server.src.routes.http.v1.auth import auth_user
from daily_tasks_server.src.routes.http.v1.profile import user_profile

router = APIRouter()
router.include_router(
    auth_user.router,
    prefix="/auth",
    tags=["authentication"]
)

router.include_router(
    user_profile.router,
    prefix="/profile",
    tags=["profile"]
)
