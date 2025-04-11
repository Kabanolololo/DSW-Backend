from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relacja z grocery_items
    grocery_items = relationship("GroceryItem", back_populates="user")