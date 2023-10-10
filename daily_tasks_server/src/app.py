from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.routes.http.router import api_router
from daily_tasks_server.src.middlewares.logging import LoggingAndProcessTime


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=Config.CORS_ORIGIN_ALLOWED,
        allow_credentials=Config.CORS_CREDENTIALS,
        allow_methods=Config.CORS_METHODS_ALLOWED,
        allow_headers=Config.CORS_HEADERS_ALLOWED,
    )
    app.add_middleware(LoggingAndProcessTime)
    app.include_router(api_router, prefix=Config.APP_API_ROUTE)

    return app
