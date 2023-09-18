from fastapi import FastAPI

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.routes.http.router import api_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(api_router, prefix=Config.APP_API_ROUTE)

    return app
