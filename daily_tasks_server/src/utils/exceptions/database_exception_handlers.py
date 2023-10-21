from fastapi import Request, status
from fastapi.responses import JSONResponse
from psycopg2 import OperationalError, IntegrityError, DataError


def database_operational_error_handler(request: Request, exc: OperationalError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "0001",
            "message": str(exc),
        }
    )


def integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": exc.pgcode,
            "message": exc.pgerror,
        }
    )


def data_error_handler(request: Request, exc: DataError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": exc.pgcode,
            "message": exc.pgerror,
        }
    )
