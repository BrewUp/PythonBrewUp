from diator.events import Event
from diator.requests import RequestHandler

from L80_Infrastructure.Sales.SalesOrderRepository import SalesOrderRepository
from src.L30_Shared.Repositories.EventStoreRepository import EventStoreRepository

from ...Domain.Entities.SalesOrder import SalesOrder
from ...Messages.Commands.CreateSalesOrder import CreateSalesOrder


class CreateSalesOrderCommandHandler(RequestHandler[CreateSalesOrder, None]):
    def __init__(self, repository: EventStoreRepository, *args, **kwargs) -> None:
        self._events: list[Event] = []
        self.repository = repository

    @property
    def events(self) -> list[Event]:
        return self._events

    def handle(self, request: CreateSalesOrder) -> None:
        sales_order = SalesOrder.create_sales_order(
            salesOrder_id=request.salesOrder_id,
            salesOrder_number=request.salesOrder_number,
            customer_id=request.customer_id,
            customer_name=request.customer_name,
        )
        # TODO inserimento in db documentale degli uncommited_events utilizzando l'id dell'aggregato (SalesOrder)
        self.repository.save(sales_order=sales_order)
        self._events = sales_order.committed_events
