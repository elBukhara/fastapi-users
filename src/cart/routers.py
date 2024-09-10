from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated

from .schemas import CartCreate, Cart
from .repository import CartRepository

router = APIRouter(
    prefix="/carts",
    tags=["Carts"]
)

@router.post("/add_to_cart")
async def add_to_cart(
    cart: Annotated[CartCreate, Depends()]
):
    response = await CartRepository.add_to_cart(cart)
    return response

@router.delete("/delete_cart/{cart_id}")
async def delete_cart(cart_id: int):
    response = await CartRepository.delete_cart(cart_id)
    return response

@router.get("/user_cart/{user_id}")
async def get_user_cart(user_id: int) -> list[Cart]:
    cart_items = await CartRepository.get_user_cart(user_id)
    return cart_items

@router.put("/decrement_quantity/{user_id}/{cart_id}")
async def decrement_quantity_of_item_in_cart(user_id: int, cart_id: int):
    response = await CartRepository.decrement_quantity_of_item_in_cart(user_id=user_id, cart_id=cart_id)
    
    return response