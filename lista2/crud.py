from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from models import Coffee
from schemas import CreateCoffee, UpdateCoffee

# Funkcja do tworzenia kawy w db
def create_coffee(db: Session, coffee: CreateCoffee):
    try:
        db_coffee = Coffee(**coffee.dict())
        db.add(db_coffee)
        db.commit()
        db.refresh(db_coffee)
        return db_coffee
    except IntegrityError:
        db.rollback()
        raise

# Funkcja do wyświetlania wszystkich kaw w db
def get_coffees(db: Session):
    return db.query(Coffee).all()

# Funkcja do wyswietlania konkrentej kawy w db
def get_coffee(db: Session, coffee_id: int):
    coffee = db.query(Coffee).filter(Coffee.id == coffee_id).first()
    if not coffee:
        raise HTTPException(status_code=404, detail="Coffee not found")
    return coffee

# Funkcja do usunięcia kawy
def delete_coffee(db: Session, coffee_id: int):
    coffee = db.query(Coffee).filter(Coffee.id == coffee_id).first()
    if not coffee:
        raise HTTPException(status_code=404, detail="Coffee not found")
    
    db.delete(coffee)
    db.commit()
    return {"message": "Coffee successfully deleted"}

# Funkcja do zupdatowania kawy
def update_coffee(db: Session, coffee_id: int, coffee_data: UpdateCoffee):
    coffee = db.query(Coffee).filter(Coffee.id == coffee_id).first()
    if not coffee:
        raise HTTPException(status_code=404, detail="Coffee not found")
    
    if coffee_data.name is not None:
        coffee.name = coffee_data.name

    if coffee_data.description is not None:
        coffee.description = coffee_data.description

    if coffee_data.price is not None:
        coffee.price = coffee_data.price

    db.commit()
    db.refresh(coffee)
    return coffee