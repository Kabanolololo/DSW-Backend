from sqlalchemy.orm import Session
from models.item import GroceryItem
from schemas.item import GroceryItemCreate

# Funkcja do pobierania wszystkich elementów z bazy danych
def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    Funkcja zwracająca listę wszystkich elementów z bazy danych
    Parametry:
    - db: sesja bazy danych
    - skip: liczba pomijanych rekordów (do paginacji)
    - limit: liczba zwracanych rekordów
    """
    pass

# Funkcja do tworzenia nowego elementu w bazie danych
def create_item(db: Session, item: GroceryItemCreate):
    """
    Funkcja tworząca nowy element w bazie danych
    Parametry:
    - db: sesja bazy danych
    - item: dane nowego elementu do zapisania
    """
    pass

# Funkcja do pobierania elementu po ID
def get_item_by_id(db: Session, item_id: int):
    """
    Funkcja zwracająca szczegóły elementu na podstawie ID
    Parametry:
    - db: sesja bazy danych
    - item_id: ID elementu do pobrania
    """
    pass

# Funkcja do aktualizowania istniejącego elementu
def update_item(db: Session, item_id: int, updated_item: GroceryItemCreate):
    """
    Funkcja aktualizująca istniejący element na podstawie ID
    Parametry:
    - db: sesja bazy danych
    - item_id: ID elementu do zaktualizowania
    - updated_item: dane do zaktualizowania w elemencie
    """
    pass

# Funkcja do usuwania elementu z bazy danych
def delete_item(db: Session, item_id: int):
    """
    Funkcja usuwająca element z bazy danych na podstawie ID
    Parametry:
    - db: sesja bazy danych
    - item_id: ID elementu do usunięcia
    """
    pass