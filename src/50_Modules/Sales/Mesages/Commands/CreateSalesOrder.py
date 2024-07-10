import dataclasses

from BrewUp.Sales.SharedKernel.DomainIds.SalesOrderId import SalesOrderId
from BrewUp.Sales.SharedKernel.CustomTypes.SalesOrderNumber import SalesOrderNumber
from diator.requests import Request

@dataclasses.dataclass(frozen=True, kw_only=True)
class CreateSalesOrder(Request):
    salesOrder_id: SalesOrderId = dataclasses.field(default="123")
    salesOrder_number: SalesOrderNumber = dataclasses.field(default="123")