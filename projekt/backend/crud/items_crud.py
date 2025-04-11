from sqlalchemy.orm import Session
from models.item import GroceryItem
from schemas.item import GroceryItemCreate
from fastapi import HTTPException, status

# Funkcja do pobierania elementów z bazy danych z filtrami i sortowaniem
def get_items(db: Session, name: str = None, category: str = None, purchased: bool = None, sort_by: str = None, sort_order: str = "asc"):
    try:
        query = db.query(GroceryItem) 
        if name:
            query = query.filter(GroceryItem.name.ilike(f"%{name}%"))
        if category:
            query = query.filter(GroceryItem.category.ilike(f"%{category}%"))
        if purchased is not None:
            query = query.filter(GroceryItem.purchased == purchased)
            
        if sort_by == "createdAt":
            if sort_order == "asc":
                query = query.order_by(GroceryItem.createdAt.asc())
            else:
                query = query.order_by(GroceryItem.createdAt.desc())
        elif sort_by == "updatedAt":
            if sort_order == "asc":
                query = query.order_by(GroceryItem.updatedAt.asc())
            else:
                query = query.order_by(GroceryItem.updatedAt.desc())

        items = query.all()

        if not items:
            raise HTTPException(status_code=404, detail="No items found matching the given criteria")

        return items

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Funkcja do tworzenia nowego elementu w bazie danych
def create_item(db: Session, item: GroceryItemCreate):
    try:
        db_item = GroceryItem(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Funkcja do pobierania elementu po ID
def crud_get_item_by_id(db: Session, item_id: int):
    try:
        db_item = db.query(GroceryItem).filter(GroceryItem.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return db_item
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Funkcja do aktualizowania istniejącego elementu w bazie danych
def update_grocery_item(db: Session, item_id: int, updated_item: GroceryItemCreate):
    try:
        db_item = db.query(GroceryItem).filter(GroceryItem.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

        db_item.name = updated_item.name
        db_item.quantity = updated_item.quantity
        db_item.unit = updated_item.unit
        db_item.category = updated_item.category
        db_item.notes = updated_item.notes

        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Funkcja do usuwania elementu z bazy danych
def delete_grocery_item(db: Session, item_id: int):
    try:
        db_item = db.query(GroceryItem).filter(GroceryItem.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

        db.delete(db_item)
        db.commit()
        return db_item
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
