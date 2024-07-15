import dataclasses
import uuid

from diator.requests import Request

from ...SharedKernel.CustomTypes.SalesOrderNumber import SalesOrderNumber
from ...SharedKernel.DomainIds import SalesOrderId


@dataclasses.dataclass(frozen=True, kw_only=True)
class CreateSalesOrder(Request):
    salesOrder_id: SalesOrderId = dataclasses.field(default=uuid.uuid4())
    salesOrder_number: SalesOrderNumber = dataclasses.field(default="123")

    customer_id: uuid.UUID
    customer_name: str
