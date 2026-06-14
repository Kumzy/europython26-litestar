from litestar import Litestar, get
from litestar.di import Provide


async def get_session() -> dict[str, str]:
    """Per-request resource — built fresh on every request."""
    return {"scope": "request"}


_client = {"scope": "app"}


async def get_client() -> dict[str, str]:
    """Per-app resource — built once, then cached."""
    return _client


# region scopes
# scope == lifetime
Provide(get_session)  # per request
Provide(get_client, use_cache=True)  # per app

# override anywhere in the layer tree:
# app  >  router / controller  >  handler
# endregion


@get("/")
async def index(session: dict[str, str], client: dict[str, str]) -> dict[str, str]:
    return {"session": session["scope"], "client": client["scope"]}


app = Litestar(
    [index],
    dependencies={
        "session": Provide(get_session),
        "client": Provide(get_client, use_cache=True),
    },
)
