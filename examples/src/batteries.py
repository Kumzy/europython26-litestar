"""Slide 20: Advanced Alchemy — the repository & service you didn't have to write.

Reuses the ``Order`` model from ``dtos.py`` (one model per SQLAlchemy registry).
"""

from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from dtos import Order


# region service
class OrderRepository(SQLAlchemyAsyncRepository[Order]):
    model_type = Order


class OrderService(SQLAlchemyAsyncRepositoryService[Order]):
    repository_type = OrderRepository
    # create · get · list · update · delete · upsert
    # + filtering, pagination, to_schema — done
    # endregion
