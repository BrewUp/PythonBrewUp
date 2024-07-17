from diator.events import Event
from diator.requests import RequestHandler

from ...Domain.Entities.SalesOrder import SalesOrder
from ...Messages.Commands.CloseSalesOrder import CloseSalesOrder


class CloseSalesOrderCommandHandler(RequestHandler[CloseSalesOrder, None]):
    def __init__(self) -> None:
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: CloseSalesOrder) -> None:
        # Ritorna un'istanza di SalesOrder con committed_events avvalorata con gli eventi nel db documentale
        # sales_order = SalesOrderRepository.get_by_id(request.salesOrder_id)
        # 
        # sales_order.apply_committed_events()
        # sales_order = sales_order.close_sales_order(
        #     salesOrder_id=request.salesOrder_id,
        # )
        # TODO inserimento in db documentale degli uncommited_events utilizzando l'id dell'aggregato (SalesOrder)
        # SalesOrderRepository.save(sales_order)
        self._events = sales_order
