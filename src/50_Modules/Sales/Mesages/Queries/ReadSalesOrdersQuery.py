import dataclasses
import uuid
from diator.requests import Request

@dataclasses.dataclass(frozen=True, kw_only=True)
class ReadSalesQuery(Request):
    salesOrder_id: SalesOrderId = dataclasses.field(uuid.uuid4())