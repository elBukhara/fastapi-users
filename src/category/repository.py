from fastapi import HTTPException
from sqlalchemy import select, delete

from database import async_session
from .schemas import AddCategory, AddCategoryResponse, DeleteCategoryResponse
from items.models import CategoryOrm

class CategoryRepository:
    @classmethod
    async def add_category(cls, category: AddCategory) -> int:
        async with async_session() as session:
            query = select(CategoryOrm).where(CategoryOrm.name == category.name)
            result = await session.execute(query)
            existing_category = result.scalar_one_or_none()
            
            if existing_category:
                raise HTTPException(status_code=400, detail="Category already exists. Please choose another one.")
            else:
                category_dict = category.model_dump()
                category = CategoryOrm(**category_dict)
                session.add(category)
                
                await session.flush()
                await session.commit()
                
                return AddCategoryResponse(message="Category was successfully added.", category_id=category.id)
    
    @classmethod
    async def delete_category(cls, category_id: int):
        async with async_session() as session:
            category = await session.get(CategoryOrm, category_id)
            
            if not category:
                raise HTTPException(
                    status_code=400, 
                    detail="Category does not exist."
                )
            else:    
                await session.execute(
                    delete(CategoryOrm)
                    .where(CategoryOrm.id == category_id)
                    )
                await session.flush()
                await session.commit()
                
                return DeleteCategoryResponse(message="Category was successfully deleted.", category_id=category_id)

    @classmethod
    async def get_all_categories(cls) -> list[CategoryOrm]:
        async with async_session() as session:
            query = select(CategoryOrm)
            result = await session.execute(query)
            categories = result.scalars().all()
            return categories
    
    @classmethod
    async def get_category(cls, category_id: int) -> CategoryOrm:
        async with async_session() as session:
            query = select(CategoryOrm).where(CategoryOrm.id == category_id)
            result = await session.execute(query)
            category = result.scalar_one_or_none()
            return category
    
    # TODO: add delete method of the category