def register_routes(app):
    """
    Import and register all routers.
    """
    from .routes import router as sample_router
    app.include_router(sample_router)
