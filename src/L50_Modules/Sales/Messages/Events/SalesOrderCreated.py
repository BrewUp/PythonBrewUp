import dataclasses
import uuid

from diator.events import DomainEvent

from src.L30_Shared.DomainIds.CustomerId import CustomerId
from src.L30_Shared.DomainIds.CustomerName import CustomerName

from ...SharedKernel.CustomTypes.SalesOrderNumber import SalesOrderNumber
from ...SharedKernel.DomainIds.SalesOrderId import SalesOrderId


@dataclasses.dataclass(frozen=True, kw_only=True)
class SalesOrderCreated(DomainEvent):  # will be handled by an event handler
    salesOrder_id: SalesOrderId = dataclasses.field(default=uuid.uuid4())
    salesOrder_number: SalesOrderNumber = dataclasses.field(default="")
    customer_id: CustomerId = dataclasses.field(default=uuid.uuid4())
    customer_name: CustomerName = dataclasses.field(default="")


@dataclasses.dataclass(frozen=True, kw_only=True)
class SalesOrderCreatedV2(DomainEvent):  # will be handled by an event handler
    salesOrder_id: SalesOrderId = dataclasses.field(default=uuid.uuid4())
    salesOrder_number: SalesOrderNumber = dataclasses.field(default="")
    salesOrder_state: str = dataclasses.field(default="open")
    customer_id: CustomerId = dataclasses.field(default=uuid.uuid4())
    customer_name: CustomerName = dataclasses.field(default="")
