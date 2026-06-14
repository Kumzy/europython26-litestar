from litestar import Litestar, get


@get("/hello")
async def hello() -> dict[str, str]:
    return {"msg": "hi"}


app = Litestar([hello])
