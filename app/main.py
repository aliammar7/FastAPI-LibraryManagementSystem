"""
from fastapi import FastAPI
from app.api.v1 import auth, users, books
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title = settings.PROJECT_NAME,
        version = settings.VERSION
    )


    # Auth router
    app.include_router(
        auth.router, 
        prefix = "/api/v1", 
        tags = ["Auth"]
    )


    # Users router
    app.include_router(
        users.router, 
        prefix = '/api/v1', 
        tags = ["Users"]
    )


    # Books router
    app.include_router(
        books.router, 
        prefix = "/api/v1", 
        tags = ["Books"]
    )

    return create_app


# Creating the app by calling the function
app = create_app()
"""

from fastapi import FastAPI
from app.api.v1 import auth, users, books
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        debug=True  # optional, shows detailed errors in browser
    )

    # Root endpoint
    @app.get("/", tags=["Root"])
    def read_root():
        return {"message": f"Welcome to {settings.PROJECT_NAME}!"}

    # Auth router
    app.include_router(
        auth.router,
        prefix="/api/v1/auth",
        tags=["Auth"]
    )

    # Users router
    app.include_router(
        users.router,
        prefix="/api/v1/users",
        tags=["Users"]
    )

    # Books router
    app.include_router(
        books.router,
        prefix="/api/v1/books",
        tags=["Books"]
    )

    return app  # ✅ return the app instance, not the function

# Creating the app by calling the function
app = create_app()
