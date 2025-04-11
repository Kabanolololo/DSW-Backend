from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from authorization.hash import hash_password, verify_password
from authorization.jwt import create_access_token, verify_token

# Funkcja do weryfikacji tokenu i pobierania użytkownika
def get_current_user(db: Session, token: str):
    try:
        user = verify_token(token, db)
        return user
    except HTTPException as e:
        raise e

# Funkcja sluzaca do rejestracji użytkownika
def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Użytkownik o podanej nazwie już istnieje"
        )

    hashed_password = hash_password(user.password)

    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

# Funkcja do logowowania użytkownika
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nieprawidłowa nazwa użytkownika lub hasło"
        )
    
    if not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nieprawidłowa nazwa użytkownika lub hasło"
        )
    
    access_token = create_access_token(data={"sub": user.username})
    return access_token
