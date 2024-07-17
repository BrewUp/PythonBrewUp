from dataclasses import dataclass

from src.L30_Shared.CustomTypes import AggregateRoot
from src.L30_Shared.DomainIds.CustomerId import CustomerId
from src.L30_Shared.DomainIds.CustomerName import CustomerName
from src.L50_Modules.Sales.SharedKernel.CustomTypes import SalesOrderNumber
from src.L50_Modules.Sales.SharedKernel.DomainIds import SalesOrderId

@dataclass
class SalesOrder(AggregateRoot):
  salesOrder_id: SalesOrderId
  salesOrder_number: SalesOrderNumber

  customer_id: CustomerId
  customer_name: CustomerName

  def __init__(self):
    pass

  def CreateSalesOrder(salesOrderId: SalesOrderId, salesOrderNumber: SalesOrderNumber, customerId: CustomerId, customerName: CustomerName):
    salesOrder_id = salesOrderId
    salesOrder_number = salesOrderNumber

    customer_id = customerId
    customer_name = customerName