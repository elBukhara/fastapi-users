from fastapi import APIRouter, Depends
from typing import Annotated

from .schemas import Category, AddCategory, AddCategoryResponse, DeleteCategoryResponse
from .repository import CategoryRepository

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/add_category")
async def add_category(
    category: Annotated[AddCategory, Depends()]
) -> AddCategoryResponse:
    response = await CategoryRepository.add_category(category)
    return response

@router.delete("/delete_category/{category_id}")
async def delete_category(category_id: int) -> DeleteCategoryResponse:
    response = await CategoryRepository.delete_category(category_id)
    return response

@router.get("/all_categories")
async def all_categories() -> list[Category]:
    categories = await CategoryRepository.get_all_categories()
    return categories
