"""Tripwire tests: each slide's example must import + run against current Litestar."""

import json

import pytest
from litestar.testing import AsyncTestClient

import batteries
import blocking
import controllers
import di
import dtos
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
        resp = await client.get("/orders")
    assert resp.status_code == 200
    assert resp.json() == {"db": "postgresql://db/orders"}


def test_blocking_apps_build() -> None:
    # No request (the handlers sleep for 2 s): registration is where Litestar
    # validates handler signatures and sync_to_thread usage.
    for app in (blocking.blocking_app, blocking.fixed_app):
        assert app.openapi_schema.paths is not None
        assert "/report" in app.openapi_schema.paths


def test_dto_excludes_internal_fields() -> None:
    # The declared shape is the contract: internal columns must not appear
    # anywhere in the generated OpenAPI document.
    document = json.dumps(dtos.app.openapi_schema.to_schema(), default=str)
    assert "total" in document
    assert "cost_price" not in document
    assert "internal_notes" not in document


def test_batteries_service_wires_repository() -> None:
    assert batteries.OrderService.repository_type is batteries.OrderRepository
    assert batteries.OrderRepository.model_type is dtos.Order
