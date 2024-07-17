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

    @staticmethod
    def create_sales_order(
        salesOrder_id: SalesOrderId,
        salesOrder_number: SalesOrderNumber,
        customer_id: CustomerId,
        customer_name: CustomerName,
    ):
        # TODO Salvataggio su db dell'ordine
        return SalesOrder(
            salesOrder_id=salesOrder_id,
            salesOrder_number=salesOrder_number,
            customer_id=customer_id,
            customer_name=customer_name,
        )
