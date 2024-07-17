from diator.events import Event
from diator.requests import RequestHandler
from src.L50_Modules.Sales.Domain.Entities import SalesOrder

from ...Messages.Commands.CreateSalesOrder import CreateSalesOrder


class CreateSalesOrderCommandHandler(RequestHandler[CreateSalesOrder, None]):
    def __init__(self) -> None:
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: CreateSalesOrder) -> None:
        CreateSalesOrder(request.salesOrder_id, request.salesOrder_number, request.customer_id, request.customer_name)
        self._events = SalesOrder.events