from diator.events import Event
from diator.requests import RequestHandler

from ...Messages.Commands.CreateSalesOrder import CreateSalesOrder


class CreateSalesOrderCommandHandler(RequestHandler[CreateSalesOrder, None]):
    def __init__(self, sales_api) -> None:
        self.sales_api = sales_api
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: CreateSalesOrder) -> None:
        self.sales_api.join(request.salesOrder_id, request.salesOrder_number)
        if request.is_late:
            self.sales_api.warn(request.salesOrder_number)
