from sqlalchemy.orm import Mapped, relationship

from auth.models.user import UserAuth
# from cart.models import CartOrm


class UserOrm(UserAuth):
    # carts: Mapped[list["CartOrm"]] = relationship("CartOrm", back_populates="user")
    pass