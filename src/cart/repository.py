from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from database import async_session

from items.models import ItemOrm
from .models import CartOrm
from .schemas import CartCreate, Cart, CartCreateResponse, CartDeleteResponse

# TODO: handle the response when the method refers to another method (Now it returns None)

class CartRepository:
    @classmethod
    async def add_to_cart(cls, cart: CartCreate) -> int:
        async with async_session() as session:

            existing_cart_query = select(CartOrm).where(
                CartOrm.user_id == cart.user_id,
                CartOrm.item_id == cart.item_id
                )
            result = await session.execute(existing_cart_query)
            existing_cart = result.scalar_one_or_none()
            
            if existing_cart:
                await cls.increment_quantity_of_item_in_cart(cart_quantity=cart.quantity, cart_id=existing_cart.id)
            else:            
                cart_dict = cart.model_dump()  
                cart = CartOrm(**cart_dict)
                session.add(cart)
                
                await session.flush()
                await session.commit()
            
            # Return the cart ID (either updated or newly created)
            if existing_cart:
                return CartCreateResponse(message="Item quantity was incremented in the cart.", cart_id=existing_cart.id)
            else:
                return CartCreateResponse(message="Item added to cart", cart_id=cart.id)
    
    @classmethod
    async def delete_cart(cls, cart_id: int):
        async with async_session() as session:
            cart = await session.get(CartOrm, cart_id)
            
            if not cart:
                raise HTTPException(
                    status_code=400, 
                    detail="The cart does not exist."
                )
            else:
                await session.execute(
                    delete(CartOrm)
                    .where(CartOrm.id == cart_id)
                )    
                await session.flush()
                await session.commit()
                
                return CartDeleteResponse(message="Cart was successfully deleted.", cart_id=cart_id)
    
    @classmethod
    async def get_user_cart(cls, user_id: int) -> list[Cart]:
        async with async_session() as session:
            # Load the cart items along with the item and its category
            query = (
                select(CartOrm)
                .options(
                    selectinload(CartOrm.item).selectinload(ItemOrm.category)  # Load item and category
                )
                .where(CartOrm.user_id == user_id)
            )           
            result = await session.execute(query)
            cart_items = result.scalars().all()
            return cart_items
    
    @classmethod
    async def increment_quantity_of_item_in_cart(cls, cart_quantity: int, cart_id: int):
        async with async_session() as session:
            result = await session.execute(
                update(CartOrm)
                .where(CartOrm.id == cart_id)
                .values(quantity = CartOrm.quantity + cart_quantity)
                )
            
            await session.flush()
            await session.commit()
            
            return cart_id
    
    @classmethod
    async def decrement_quantity_of_item_in_cart(cls, user_id: int, cart_id: int) -> int:
        async with async_session() as session:
            existing_cart_query = select(CartOrm).where(
                CartOrm.user_id == user_id,
                CartOrm.id == cart_id
            )
            result = await session.execute(existing_cart_query)
            existing_cart = result.scalar_one_or_none()

            if not existing_cart:
                raise ValueError("Item not found in cart")

            if existing_cart.quantity > 1:
                new_quantity = existing_cart.quantity - 1
                update_query = (
                    update(CartOrm)
                    .where(CartOrm.id == existing_cart.id)
                    .values(quantity=new_quantity)
                )
                await session.execute(update_query)
                await session.commit()
                
                return CartDeleteResponse(message="Item quantity decremented.", cart_id=existing_cart.id)
            else:
                await cls.delete_cart(existing_cart.id)
                return CartDeleteResponse(message="Cart was successfully deleted.", cart_id=existing_cart.id)
