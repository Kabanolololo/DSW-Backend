from sqlalchemy.orm import Session
from models.item import GroceryItem
from schemas.item import GroceryItemCreate
from fastapi import HTTPException, status

# Funkcja do pobierania elementów z bazy danych z filtrami i sortowaniem
def get_items(
    db: Session, 
    name: str = None, 
    category: str = None, 
    purchased: bool = None, 
    sort_by: str = None,  # Parametr dla sortowania
    sort_order: str = "asc"  # Parametr dla kierunku sortowania (rosnąco/malejąco)
):
    try:
        query = db.query(GroceryItem)  # Tworzymy zapytanie na tabeli grocery_items

        # Filtrujemy po nazwie, jeśli podano
        if name:
            query = query.filter(GroceryItem.name.ilike(f"%{name}%"))

        # Filtrujemy po kategorii, jeśli podano
        if category:
            query = query.filter(GroceryItem.category.ilike(f"%{category}%"))

        # Filtrujemy po purchased, jeśli podano
        if purchased is not None:
            query = query.filter(GroceryItem.purchased == purchased)

        # Dodanie sortowania
        if sort_by == "createdAt":
            if sort_order == "asc":
                query = query.order_by(GroceryItem.createdAt.asc())  # Sortowanie rosnąco po createdAt
            else:
                query = query.order_by(GroceryItem.createdAt.desc())  # Sortowanie malejąco po createdAt

        elif sort_by == "updatedAt":
            if sort_order == "asc":
                query = query.order_by(GroceryItem.updatedAt.asc())  # Sortowanie rosnąco po updatedAt
            else:
                query = query.order_by(GroceryItem.updatedAt.desc())  # Sortowanie malejąco po updatedAt

        items = query.all()  # Zwracamy wszystkie pasujące elementy

        if not items:  # Jeśli wynik jest pusty
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
