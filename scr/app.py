from fastapi import FastAPI

app = FastAPI(
    title="Ecommerce API",
    description="A simple e-commerce REST API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Ecommerce API is running"}