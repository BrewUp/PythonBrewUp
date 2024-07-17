import dataclasses
import uuid

from diator.requests import Request

from ...SharedKernel.DomainIds import SalesOrderId


@dataclasses.dataclass(frozen=True, kw_only=True)
class CloseSalesOrder(Request):
    salesOrder_id: SalesOrderId
