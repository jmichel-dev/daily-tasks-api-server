from fastapi import APIRouter

from daily_tasks_server.src.routes.http import v1

api_router = APIRouter()
api_router.include_router(v1.router, prefix="/v1")
