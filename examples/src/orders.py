from dataclasses import dataclass

from litestar import Litestar, get
from litestar.connection import ASGIConnection
from litestar.di import Provide
from litestar.handlers.base import BaseRouteHandler


@dataclass
class User:
    id: int
    name: str


@dataclass
class OrderDTO:
    id: int
    total: int


class Session:
    """Stand-in for an injected DB session."""


def require_user(connection: ASGIConnection, handler: BaseRouteHandler) -> None:
    """Guard: would reject anonymous requests (no-op stub here)."""
    return None


async def provide_user() -> User:
    return User(id=1, name="ada")


async def provide_session() -> Session:
    return Session()


# region requirements
@get("/orders", guards=[require_user])
async def list_orders(
    user: User,  # from auth
    db: Session,  # injected
    page: int = 1,
    page_size: int = 20,
    search: str | None = None,
    status: str | None = None,
    sort: str = "created_at",
) -> list[OrderDTO]:
    ...
    # endregion


app = Litestar(
    [list_orders],
    dependencies={"user": Provide(provide_user), "db": Provide(provide_session)},
)
