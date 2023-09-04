from fastapi import APIRouter

from daily_tasks_server.src.controllers.http.v1.auth import auth_user

router = APIRouter()
router.include_router(
    auth_user.router,
    prefix="/auth",
    tags=["authentication"]
)