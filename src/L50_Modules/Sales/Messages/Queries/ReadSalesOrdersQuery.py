import dataclasses
import uuid

from diator.requests import Request

from ...SharedKernel.DomainIds import SalesOrderId


@dataclasses.dataclass(frozen=True, kw_only=True)
class ReadSalesOrderQuery(Request):
    salesOrder_id: SalesOrderId = dataclasses.field(default=uuid.uuid4())
