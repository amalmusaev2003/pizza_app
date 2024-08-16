from fastapi import FastAPI

from app.routers.users import router as user_router
from app.routers.products import router as product_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to AmalPizza!"}

app.include_router(user_router)
app.include_router(product_router)



