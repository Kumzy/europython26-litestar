from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from litestar import Litestar, get
from litestar.datastructures import State
from litestar.di import NamedDependency, Provide


@dataclass
class Engine:
    """Application resource created during startup."""

    url: str


@dataclass
class Session:
    """Cheap — built fresh per request."""

    engine: Engine


# region scopes
@asynccontextmanager
async def database_lifespan(app: Litestar) -> AsyncIterator[None]:
    app.state.engine = Engine(url="postgresql://db/orders")
    yield


async def provide_session(state: State) -> Session:
    return Session(engine=state.engine)


@get("/orders")
async def list_orders(session: NamedDependency[Session]) -> dict[str, str]:
    return {"db": session.engine.url}


app = Litestar(
    route_handlers=[list_orders],
    lifespan=[database_lifespan],
    dependencies={"session": Provide(provide_session, use_cache=True)},
)
# endregion
