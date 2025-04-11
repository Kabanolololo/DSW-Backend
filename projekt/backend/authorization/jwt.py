from sqlalchemy.orm import Session
from database import SessionLocal
from datetime import datetime, timedelta
from typing import Union
from fastapi import HTTPException, status
from models.user import User
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "secret_key"  
ALGORITHM = "HS256"  
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Funkcja do generowania tokenu
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    
    # Jeśli nie podano czasu wygaśnięcia, domyślnie ustawiamy na 30 minut
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Przygotowujemy payload
    to_encode = data.copy()
    to_encode.update({"exp": expire})  
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Funkcja do weryfikowania tokenu
def verify_token(token: str, db: Session):
    try:
        # Dekodowanie tokenu i weryfikacja
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Nieprawidłowy token",
            )
        
        user = db.query(User).filter(User.username == username).first()
        
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Użytkownik nie istnieje",
            )
        
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token jest nieprawidłowy",
        )
