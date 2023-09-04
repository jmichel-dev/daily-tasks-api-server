from fastapi import FastAPI

from daily_tasks_server.src.controllers.http.router import api_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(api_router, prefix="/api")

    return app
