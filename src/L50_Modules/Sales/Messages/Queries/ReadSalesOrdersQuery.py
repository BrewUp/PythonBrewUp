import dataclasses
import uuid
from diator.requests import Request
from Sales.Values.SalesOrderId import SalesOrderId

@dataclasses.dataclass(frozen=True, kw_only=True)
class ReadSalesQuery(Request):
    salesOrder_id: SalesOrderId = dataclasses.field(uuid.uuid4())