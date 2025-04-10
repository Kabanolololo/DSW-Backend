from schemas.item import GroceryItem
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from database import Base

# Model listy zakupów dla grocery items
class GroceryItem(Base):
    __tablename__ = "grocery_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit = Column(String(20), nullable=True)
    category = Column(String(50), nullable=True)
    notes = Column(String(255), nullable=True)
    
    purchased = Column(Boolean, default=False, nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)
