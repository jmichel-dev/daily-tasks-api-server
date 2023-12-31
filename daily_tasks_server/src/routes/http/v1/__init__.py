from fastapi import APIRouter

from daily_tasks_server.src.routes.http.v1.auth import auth_user
from daily_tasks_server.src.routes.http.v1.profile import user_profile
from daily_tasks_server.src.routes.http.v1.projects import projects_router
from daily_tasks_server.src.routes.http.v1.task import task_router

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

router.include_router(
    projects_router.router,
    prefix="/project",
    tags=["project"]
)

router.include_router(
    task_router.router,
    prefix="/project",
    tags=["task"]
)
