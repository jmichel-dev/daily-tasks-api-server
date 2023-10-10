import os
import time
from uuid import uuid4

from fastapi import Request
from starlette.responses import Response
from starlette.types import ASGIApp
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class LoggingAndProcessTime(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()
        request_id = str(uuid4().hex)
        response = await call_next(request)
        process_time = time.time() - start_time
        process_time = str(round(process_time * 1000))
        response.headers["X-Process-Time-MS"] = process_time
        log_msg = f"request_id={request_id} service=my-svc url={request.url} host={request.client.host} " \
                  f"port={request.client.port} processing_time_ms={process_time} env={os.environ.get('APP_ENV')} " \
                  f"version=v1 pid={os.getpid()} region={os.environ.get('REGION')} "
        # logger.info(log_msg)
        print(log_msg)
        return response


