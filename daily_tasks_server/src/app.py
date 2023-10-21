from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from psycopg2 import OperationalError, IntegrityError, DataError

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.routes.http.router import api_router
from daily_tasks_server.src.middlewares.logging import LoggingAndProcessTime
from daily_tasks_server.src.utils.exceptions.database_exception_handlers import (
    database_operational_error_handler,
    integrity_error_handler,
    data_error_handler
)


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

    app.add_exception_handler(OperationalError, database_operational_error_handler)
    app.add_exception_handler(IntegrityError, integrity_error_handler)
    app.add_exception_handler(DataError, data_error_handler)

    return app
