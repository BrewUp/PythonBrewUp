from di import Container, bind_by_type
from di.dependent import Dependent
from diator.container.di import DIContainer
from diator.events import EventEmitter, EventMap
from diator.mediator import Mediator
from diator.message_brokers.redis import RedisMessageBroker
from diator.requests import RequestMap
from redis import asyncio as redis

from ..Domain.CommandHandlers.CreateSalesOrderCommandHandler import CreateSalesOrderCommandHandler
from ..Messages.Commands.CreateSalesOrder import CreateSalesOrder
from ..Messages.Events.SalesOrderCreated import SalesOrderCreated
from ..Messages.Queries.ReadSalesOrdersQuery import ReadSalesOrderQuery
from ..ReadModel.EventHandlers import ReadSalesOrderQueryHandler, SalesOrderCreatedEventHandler


async def setup_sales_di() -> DIContainer:
    external_container = Container()

    external_container.bind(
        bind_by_type(
            Dependent(CreateSalesOrderCommandHandler, scope="request"),
            CreateSalesOrderCommandHandler,
        )
    )

    # external_container.bind(
    #     bind_by_type(
    #         Dependent(SalesOrderCreatedEventHandler, scope="request"),
    #         SalesOrderCreatedEventHandler,
    #     )
    # )

    # external_container.bind(
    #     bind_by_type(
    #         Dependent(ReadSalesOrderQueryHandler, scope="request"),
    #         ReadSalesOrderQueryHandler,
    #     )
    # )

    container = DIContainer()
    container.attach_external_container(external_container)

    return container


async def build_sales_mediator() -> Mediator:
    # container = setup_di()
    sales_container = setup_sales_di()

    event_map = EventMap()
    event_map.bind(SalesOrderCreated, SalesOrderCreatedEventHandler)
    request_map = RequestMap()
    request_map.bind(CreateSalesOrder, CreateSalesOrderCommandHandler)
    request_map.bind(ReadSalesOrderQuery, ReadSalesOrderQueryHandler)

    redis_client = redis.Redis.from_url("redis://localhost:6379/0")
    event_emitter = EventEmitter(
        message_broker=RedisMessageBroker(redis_client),
        event_map=event_map,
        container=sales_container,
    )

    mediator = Mediator(
        request_map=request_map,
        event_emitter=event_emitter,
        container=sales_container,
    )

    return mediator
