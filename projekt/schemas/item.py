from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class GroceryItemCreate(BaseModel):
    name: str = Field(..., max_length=100, example="Milk")
    quantity: int = Field(..., ge=1, example=2)
    unit: Optional[str] = Field(None, max_length=20, example="liters")
    category: Optional[str] = Field(None, max_length=50, example="Dairy")
    notes: Optional[str] = Field(None, max_length=255, example="Lactose-free")

class GroceryItem(GroceryItemCreate):
    id: int
    createdAt: datetime
    updatedAt: datetime
    purchased: bool = False

class Error(BaseModel):
    message: str
    details: Optional[str] = None
