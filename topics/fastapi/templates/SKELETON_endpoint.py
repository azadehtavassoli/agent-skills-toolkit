from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import register_routes
from app.settings import get_settings
from app.exceptions import register_exception_handlers

def create_app() -> FastAPI:
    """
    Create FastAPI app instance with layered structure,
    DI settings, CORS, routes, and error handlers.
    """
    settings = get_settings()

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.API_VERSION,
    )

    # CORS config
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register custom exception handlers
    register_exception_handlers(app)

    # Register routers
    register_routes(app)

    return app


app = create_app()
