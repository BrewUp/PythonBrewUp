import dataclasses
import uuid
from diator.requests import Request
from Sales.Values.SalesOrderId import SalesOrderId
from Sales.Values.SalesOrderNumber import SalesOrderNumber

@dataclasses.dataclass(frozen=True, kw_only=True)
class CreateSalesOrder(Request):
    salesOrder_id: SalesOrderId = dataclasses.field(uuid.uuid4())
    salesOrder_number: SalesOrderNumber = dataclasses.field(default="123")

    customer_id: uuid.UUID
    customer_name: str
