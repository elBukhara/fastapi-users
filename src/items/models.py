from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional, List

from database import Base

class CategoryOrm(Base):
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    
    # Relationship: one category can have multiple items
    items: Mapped[List["ItemOrm"]] = relationship("ItemOrm", back_populates="category")

class ItemOrm(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]]
    
    # Foreign key linking to Category
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    
    # Relationship: the item belongs to a category
    category: Mapped["CategoryOrm"] = relationship("CategoryOrm", back_populates="items")
