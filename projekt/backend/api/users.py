from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from crud.user_crud import create_user, authenticate_user
from api.dependencies import get_db

router = APIRouter()

# Endpoint do rejestracji użytkownika
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db=db, user=user)
        return {"message": "User created successfully"}
    except HTTPException as e:
        raise e  
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint logowania
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(db, user.username, user.password)
    return {"message": "Zalogowano pomyślnie"}