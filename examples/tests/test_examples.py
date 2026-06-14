"""Tripwire tests: each slide's example must import + run against current Litestar."""

import pytest
from litestar.testing import AsyncTestClient

import controllers
import di
import hello
import orders


@pytest.mark.anyio
async def test_hello_returns_greeting() -> None:
    async with AsyncTestClient(app=hello.app) as client:
        resp = await client.get("/hello")
    assert resp.status_code == 200
    assert resp.json() == {"msg": "hi"}


def test_orders_app_builds_and_documents_route() -> None:
    # No request: handler body is `...`. We only prove the app constructs and
    # OpenAPI generates — that catches guard / DI / DTO signature drift.
    schema = orders.app.openapi_schema
    assert schema.paths is not None
    assert "/orders" in schema.paths


@pytest.mark.anyio
async def test_controller_lists_orders() -> None:
    async with AsyncTestClient(app=controllers.app) as client:
        resp = await client.get("/orders")
    assert resp.status_code == 200
    assert resp.json() == [{"id": 1, "total": 42}]


@pytest.mark.anyio
async def test_di_scopes_resolve() -> None:
    async with AsyncTestClient(app=di.app) as client:
        resp = await client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"session": "request", "client": "app"}
