import dataclasses

from diator.events import DomainEvent, NotificationEvent, ECSTEvent
from Sales.Values.SalesOrderId import SalesOrderId
from Sales.Values.SalesOrderNumber import SalesOrderNumber

@dataclasses.dataclass(frozen=True, kw_only=True)
class SalesOrderCreated(DomainEvent):  # will be handled by an event handler
    salesOrder_id: SalesOrderId = dataclasses.field(default="123")
    salesOrder_number: SalesOrderNumber = dataclasses.field(default="123")