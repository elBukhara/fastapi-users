from pydantic import BaseModel
from typing import Optional

from category.schemas import Category

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    category_id: int  # TODO: define if Category is required/optional

class AddItem(ItemBase):
    pass

class Item(ItemBase):
    id: int
    category: Optional[Category]  # Include the category information

    class Config:
        orm_mode = True

class AddItemResponse(BaseModel):
    message: str
    item_id: int

class DeleteItemResponse(AddItemResponse):
    pass