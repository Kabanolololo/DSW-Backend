from pydantic import BaseModel, Field, validator
from typing import Optional

# Schemat do rejestracji
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, example="johndoe")
    password: str = Field(..., min_length=6, max_length=100, example="strongpassword123")
    repeated_password: str = Field(..., min_length=6, max_length=100, example="strongpassword123")

    @validator("repeated_password")
    def passwords_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Hasła muszą się zgadzać")
        return v

    class Config:
        anystr_strip_whitespace = True

# Schemat do logowania
class UserLogin(BaseModel):
    username: str
    password: str