from pydantic import BaseModel, constr, confloat
from typing import Optional

class CoffeeBase(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: str
    price: confloat(gt=0)
    
    class Config:
        orm_mode = True
    
class CreateCoffee(CoffeeBase):
    pass

class UpdateCoffee(BaseModel):
    name: Optional[constr(min_length=1, max_length=100)] = None
    description: Optional[str] = None
    price: Optional[confloat(gt=0)] = None