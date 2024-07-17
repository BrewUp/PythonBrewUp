from diator.events import Event
from diator.requests import RequestHandler

from ...Domain.Entities.SalesOrder import SalesOrder
from ...Messages.Commands.CreateSalesOrder import CreateSalesOrder


class CreateSalesOrderCommandHandler(RequestHandler[CreateSalesOrder, None]):
    def __init__(self) -> None:
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: CreateSalesOrder) -> None:
        sales_order = SalesOrder.create_sales_order(
            salesOrder_id=request.salesOrder_id,
            salesOrder_number=request.salesOrder_number,
            customer_id=request.customer_id,
            customer_name=request.customer_name,
        )
        self._events = sales_order.events
