import asyncio

from di import Container, bind_by_type
from di.dependent import Dependent
from diator.container.di import DIContainer
from diator.mediator import Mediator
from diator.message_brokers.redis import RedisMessageBroker
from fastapi import FastAPI
from redis import asyncio as redis

from src.L50_Modules.Sales.Domain.CommandHandlers.CreateSalesOrderCommandHandler import (
    CreateSalesOrderCommandHandler,
)
from src.L50_Modules.Sales.Messages.Commands.CreateSalesOrder import CreateSalesOrder
from src.L50_Modules.Sales.Messages.Events.SalesOrderCreated import SalesOrderCreated
from src.L50_Modules.Sales.Messages.Queries.ReadSalesOrdersQuery import (
    ReadSalesOrderQuery,
)

from .endpoints import router

# from src.L50_Modules.Sales.ReadModel.EventHandlers.SalesOrderCreatedEventHandler import (
#     SalesOrderCreatedEventHandler,
# )


app = FastAPI()


def setup_di() -> DIContainer:
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


async def build_mediator() -> Mediator:
    container = setup_di()

    event_map = EventMap()
    event_map.bind(SalesOrderCreated, SalesOrderCreatedEventHandler)
    request_map = RequestMap()
    request_map.bind(CreateSalesOrder, CreateSalesOrderCommandHandler)
    request_map.bind(ReadSalesOrderQuery, ReadSalesOrderQueryHandler)

    redis_client = redis.Redis.from_url("redis://localhost:6379/0")
    event_emitter = EventEmitter(
        message_broker=RedisMessageBroker(redis_client),
        event_map=event_map,
        container=container,
    )

    mediator = Mediator(
        request_map=request_map,
        event_emitter=event_emitter,
        container=container,
    )

    return mediator


async def main() -> None:

    mediator = build_mediator()
    app.include_router(router)

    # response = await mediator.send(ReadMeetingQuery(meeting_id=57))

    # assert isinstance(response, ReadMeetingQueryResult)


if __name__ == "__main__":
    asyncio.run(main())
