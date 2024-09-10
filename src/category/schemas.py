from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class AddCategory(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class AddCategoryResponse(BaseModel):
    message: str
    category_id: int

class DeleteCategoryResponse(AddCategoryResponse):
    pass