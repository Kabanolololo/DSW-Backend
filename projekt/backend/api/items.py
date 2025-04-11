from fastapi import APIRouter, HTTPException, status, Depends, Header
from typing import List
from sqlalchemy.orm import Session
from schemas.item import GroceryItem, GroceryItemCreate, ItemQueryParams
from crud.items_crud import get_items, create_item, crud_get_item_by_id, update_grocery_item, delete_grocery_item
from api.dependencies import get_db

router = APIRouter()

# Endpoint do pobierania wszystkich elementów z filtrowaniem i sortowaniem
@router.get("/items/", response_model=List[GroceryItem])
def list_items(db: Session = Depends(get_db), query_params: ItemQueryParams = Depends(), token: str = Header(...)):
    items = get_items(db=db,token=token,name=query_params.name,category=query_params.category,purchased=query_params.purchased,sort_by=query_params.sort_by,sort_order=query_params.sort_order)
    return items

# Endpoint do tworzenia nowego elementu
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_item(item: GroceryItemCreate, db: Session = Depends(get_db), token: str = Header(...)):
    return create_item(db=db, item=item, token=token)

# Endpoint do pobierania elementu po ID
@router.get("/{item_id}", response_model=GroceryItem)
def get_item_by_id(item_id: int, db: Session = Depends(get_db), token: str = Header(...)):
    db_item = crud_get_item_by_id(db=db, item_id=item_id, token=token)
    return db_item

# Endpoint do aktualizowania elementu po ID
@router.put("{item_id}", response_model=GroceryItem)
def update_item(item_id: int, updated: GroceryItemCreate, db: Session = Depends(get_db),token: str = Header(...)):
    db_item = update_grocery_item(db=db, item_id=item_id, updated_item=updated, token=token)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Endpoint do usuwania elementu
@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
def delete_item(item_id: int, db: Session = Depends(get_db),token: str = Header(...)):
    db_item = delete_grocery_item(db=db, item_id=item_id, token=token)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item successfully deleted"}
