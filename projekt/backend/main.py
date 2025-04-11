from fastapi import FastAPI, Depends, HTTPException, status
from database import SessionLocal, engine, Base
from models import item
from api.items import router as items_router
from api.users import router as user_router

# Tworzymy tabele w bazie danych
Base.metadata.create_all(bind=engine)

# Tworzymy aplikację FastAPI
app = FastAPI(
    title="Grocery List Management API",
    description="A simple REST API for managing a grocery shopping list, designed for student term projects.",
    version="1.0.0",
    contact={
        "name": "University Course Staff",
        "email": "support@example.edu"
    }
)

app.include_router(items_router, prefix="/items", tags=["grocery-items"])
app.include_router(user_router, prefix="/users", tags=["user"])



