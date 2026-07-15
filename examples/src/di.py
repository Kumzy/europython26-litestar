from dataclasses import dataclass

from litestar import Litestar, get
from litestar.di import NamedDependency, Provide


@dataclass
class HttpClient:
    """Expensive — built once per app."""

    base_url: str


@dataclass
class WeatherService:
    """Cheap — built fresh per request."""

    client: HttpClient


# region scopes
async def provide_client() -> HttpClient:
    return HttpClient(base_url="https://api.weather.example")


async def provide_weather(client: NamedDependency[HttpClient]) -> WeatherService:
    return WeatherService(client=client)


@get("/forecast")
async def forecast(weather: NamedDependency[WeatherService]) -> dict[str, str]:
    return {"upstream": weather.client.base_url}


app = Litestar(
    route_handlers=[forecast],
    dependencies={
        "client": Provide(provide_client, use_cache=True),  # app: built once
        "weather": Provide(provide_weather),  # request: fresh each time
    },
)
# endregion
