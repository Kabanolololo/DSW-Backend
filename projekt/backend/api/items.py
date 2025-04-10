from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.orm import Session
from schemas.item import GroceryItem, GroceryItemCreate, ItemQueryParams
from crud.items_crud import get_items, create_item, crud_get_item_by_id, update_grocery_item, delete_grocery_item
from api.dependencies import get_db

router = APIRouter()

# Endpoint do pobierania wszystkich elementów z filtrowaniem i sortowaniem
@router.get("/", response_model=List[GroceryItem])
def list_items(
    db: Session = Depends(get_db),
    query_params: ItemQueryParams = Depends(),  # Przyjmujemy parametry zapytania jako obiekt
):
    # Wywołujemy funkcję CRUD do pobierania elementów z bazy danych
    items = get_items(
        db,
        name=query_params.name,
        category=query_params.category,
        purchased=query_params.purchased,
        sort_by=query_params.sort_by,
        sort_order=query_params.sort_order
    )
    return items

# Endpoint do tworzenia nowego elementu
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_item(item: GroceryItemCreate, db: Session = Depends(get_db)):
    create_item(db=db, item=item)
    return {"message": "Successfully added item"}


# Endpoint do pobierania elementu po ID
@router.get("/{item_id}", response_model=GroceryItem)
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    db_item = crud_get_item_by_id(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Endpoint do aktualizowania istniejącego elementu
@router.put("/{item_id}", response_model=GroceryItem)
def update_item(item_id: int, updated: GroceryItemCreate, db: Session = Depends(get_db)):
    db_item = update_grocery_item(db=db, item_id=item_id, updated_item=updated)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Endpoint do usuwania elementu
@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = delete_grocery_item(db=db, item_id=item_id)
    
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"message": "Item successfully deleted"}
