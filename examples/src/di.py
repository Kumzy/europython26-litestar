from dataclasses import dataclass

from litestar import Litestar, get
from litestar.di import NamedDependency, Provide


@dataclass
class Engine:
    """Expensive — built once per app."""

    url: str


@dataclass
class Session:
    """Cheap — built fresh per request."""

    engine: Engine


# region scopes
async def provide_engine() -> Engine:
    return Engine(url="postgresql://db/orders")


async def provide_session(engine: NamedDependency[Engine]) -> Session:
    return Session(engine=engine)


@get("/orders")
async def list_orders(session: NamedDependency[Session]) -> dict[str, str]:
    return {"db": session.engine.url}


app = Litestar(
    route_handlers=[list_orders],
    dependencies={
        "engine": Provide(provide_engine, use_cache=True),  # app: built once
        "session": Provide(provide_session),  # request: fresh each time
    },
)
# endregion
