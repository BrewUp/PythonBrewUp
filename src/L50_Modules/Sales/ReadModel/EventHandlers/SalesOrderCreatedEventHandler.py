from diator.events import EventHandler

from ...Messages.Commands.CreateSalesOrder import CreateSalesOrder
from ...Messages.Events import SalesOrderCreated


class SalesOrderCreatedEventHandler(EventHandler[CreateSalesOrder]):
    def __init__(self, create_sales_order: CreateSalesOrder) -> None:
        self._create_sales_order = create_sales_order

    async def handle(self, event: SalesOrderCreated) -> None:
        await self._create_sales_order.notify(event.SalesOrderId, "New user joined!")
