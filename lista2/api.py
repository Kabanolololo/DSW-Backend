from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from typing import List
import schemas
import crud

router = APIRouter()

# Endpoint do tworzenia kawy
@router.post("/coffees/", response_model=schemas.CoffeeBase, status_code=status.HTTP_201_CREATED)
def create_coffeee(coffee: schemas.CreateCoffee, db: Session = Depends(get_db)):
    try:
        return crud.create_coffee(db=db, coffee=coffee)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Coffee already in db"
        )

# Endpoint do wyswietlania wszystkich notatek
@router.get("/coffees/",response_model=List[schemas.CoffeeBase])
def get_coffees(db: Session = Depends(get_db)):
    try: 
        coffees = crud.get_coffees(db)
        if not coffees:
            raise HTTPException(
                status_code=status.HTTP_404,
                detail="No coffees found"
            )
        return coffees
    except Exception as e:
        raise HTTPException(status_code=500, detail="DB error")

# Endpoint do wyswietlania konkretnej kawy
@router.get("/coffee/{coffee_id}", response_model=schemas.CoffeeBase)
def get_coffee(coffee_id: int, db: Session = Depends(get_db)):
    return crud.get_coffee(db, coffee_id)

# Endpoint do usunięcia kawy
@router.delete("/coffees/{id}")
def delete_coffee(id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_coffee(db=db, coffee_id=id)
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="DB error during delete")
    
# Endpoint do zaktualizowania kawy
@router.put("/coffee/{id}", response_model=schemas.CoffeeBase)
def update_coffee(id: int, coffee: schemas.UpdateCoffee, db: Session = Depends(get_db)):
    try:
        return crud.update_coffee(db=db, coffee_id=id, coffee_data=coffee)
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="DB error during update")