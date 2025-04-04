from fastapi import FastAPI
from database import init_db
from api import router as coffee_router

app = FastAPI()

app.include_router(coffee_router, prefix="/api")
