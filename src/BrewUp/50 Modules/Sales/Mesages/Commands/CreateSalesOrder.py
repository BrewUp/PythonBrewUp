from BrewUp.Sales.SharedKernel.DomainIds.SalesOrderId import SalesOrderId
from BrewUp.Sales.SharedKernel.CustomTypes.SalesOrderNumber import SalesOrderNumber
from dataclasses import dataclasses
from diator.requests import Request
from diator.response import Response

@dataclasses.dataclass(frozen=True, kw_only=True)
class CreateSalesOrder(Request):
    salesOrder_id: SalesOrderId = dataclasses.field(default="123")
    salesOrder_number: SalesOrderNumber = dataclasses.field(default="123")