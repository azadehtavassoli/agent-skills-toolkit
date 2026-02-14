from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException as FastAPIHTTPException

class AppError(Exception):
    """
    Domain exception with structured detail.
    """
    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code
        super().__init__(message)

def register_exception_handlers(app: FastAPI):
    """
    Register global exception handlers.
    """

    @app.exception_handler(AppError)
    async def handle_app_error(request: Request, exc: AppError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"code": exc.code, "message": exc.message},
        )

    @app.exception_handler(FastAPIHTTPException)
    async def handle_fastapi_http(request: Request, exc: FastAPIHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"code": "http_error", "message": exc.detail},
        )
