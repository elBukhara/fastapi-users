from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Integer

from database import Base

class CartOrm(Base):
    __tablename__ = "carts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    
    user = relationship("UserOrm", back_populates="carts")
    item = relationship("ItemOrm")
    