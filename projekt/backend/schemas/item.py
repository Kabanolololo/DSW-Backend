from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class UnitEnum(str, Enum):
    liters = "liters"
    kilograms = "kg"
    pieces = "pcs"

# Schemat do tworzenia nowego elementu
class GroceryItemCreate(BaseModel):
    name: str = Field(..., max_length=100, example="Milk")
    quantity: int = Field(..., ge=1, example=2)
    unit: Optional[UnitEnum] = Field(None, example="liters")
    category: Optional[str] = Field(None, max_length=50, example="Dairy")
    notes: Optional[str] = Field(None, max_length=255, example="Lactose-free")
    #user_id: int = Field(..., example=1)

    class Config:
        anystr_strip_whitespace = True

# Schemat dla elementu, który jest zwracany po utworzeniu
class GroceryItem(GroceryItemCreate):
    id: int
    createdAt: datetime 
    updatedAt: datetime  
    purchased: bool = False 

    class Config:
        anystr_strip_whitespace = True

# Schemat dla filtorwania i sortowania
class ItemQueryParams(BaseModel):
    name: Optional[str] = Field(None, max_length=100, example="Milk")  
    category: Optional[str] = Field(None, max_length=50, example="Dairy") 
    purchased: Optional[bool] = Field(None, example=True) 
    sort_by: Optional[str] = Field(None, example="createdAt", enum=["createdAt", "updatedAt"])
    sort_order: Optional[str] = Field("asc", example="asc", enum=["asc", "desc"])

    class Config:
        anystr_strip_whitespace = True
