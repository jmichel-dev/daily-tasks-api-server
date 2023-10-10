from fastapi import FastAPI

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.routes.http.router import api_router
from daily_tasks_server.src.middlewares.logging import LoggingAndProcessTime


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(LoggingAndProcessTime)
    app.include_router(api_router, prefix=Config.APP_API_ROUTE)

    return app
