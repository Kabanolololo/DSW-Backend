from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.item import GroceryItem, GroceryItemCreate

router = APIRouter()

# Endpoint do pobierania wszystkich elementów
@router.get("/", response_model=List[GroceryItem])
def list_items():
    raise HTTPException(status_code=501, detail="Not implemented")

# Endpoint do tworzenia nowego elementu
@router.post("/", response_model=GroceryItem, status_code=status.HTTP_201_CREATED)
def add_item(item: GroceryItemCreate):
    raise HTTPException(status_code=501, detail="Not implemented")

# Endpoint do pobierania elementu po ID
@router.get("/{item_id}", response_model=GroceryItem)
def get_item_by_id(item_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")

# Endpoint do aktualizowania istniejącego elementu
@router.put("/{item_id}", response_model=GroceryItem)
def update_item(item_id: int, updated: GroceryItemCreate):
    raise HTTPException(status_code=501, detail="Not implemented")

# Endpoint do usuwania elementu
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    raise HTTPException(status_code=501, detail="Not implemented")
