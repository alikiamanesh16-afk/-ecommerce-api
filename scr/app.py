
from fastapi import FastAPI

from scr.api.endpoints.v1.router import router

app = FastAPI(
    title="Ecommerce API",
    description="A simple e-commerce REST API",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")
