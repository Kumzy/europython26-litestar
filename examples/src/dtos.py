"""Slide 18: declare the response shape — internal fields never reach the wire."""

from uuid import UUID

from advanced_alchemy.base import UUIDBase
from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar import Litestar, get
from sqlalchemy.orm import Mapped


# region dto
class Order(UUIDBase):
    total: Mapped[int]
    status: Mapped[str]
    cost_price: Mapped[int]  # internal
    internal_notes: Mapped[str]  # internal


class OrderOut(SQLAlchemyDTO[Order]):
    config = SQLAlchemyDTOConfig(
        exclude={"cost_price", "internal_notes"},
    )


@get("/orders/{order_id:uuid}", return_dto=OrderOut)
async def get_order(order_id: UUID) -> Order:
    ...
    # endregion


app = Litestar([get_order])
