from dataclasses import dataclass

from litestar import Litestar, get
from litestar.controller import Controller
from litestar.di import NamedDependency, Provide


@dataclass
class OrderDTO:
    id: int
    total: int


class OrderService:
    async def list(self) -> list[OrderDTO]:
        return [OrderDTO(id=1, total=42)]


async def order_svc() -> OrderService:
    return OrderService()


# region controller
class OrderController(Controller):
    path = "/orders"
    dependencies = {"svc": Provide(order_svc)}

    @get()
    async def list(self, svc: NamedDependency[OrderService]) -> list[OrderDTO]:
        return await svc.list()


app = Litestar(route_handlers=[OrderController])
# endregion
