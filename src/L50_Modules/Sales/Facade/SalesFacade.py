import uuid

from src.L30_Shared.DomainIds import CustomerId, CustomerName

from ..Facade.SalesHelper import build_sales_mediator
from ..Messages.Commands.CreateSalesOrder import CreateSalesOrder
from ..SharedKernel.Contracts import CreateSalesOrderContract
from ..SharedKernel.CustomTypes import SalesOrderNumber


class SalesFacade:
    def create_sales_order(self, create_sales_order_contract: CreateSalesOrderContract):
        # Se vogliamo verificare se l'id esiste lo facciamo qui
        # Potremmo creare un oggetto Customer in cui ci sono più informazioni
        create_sales_order = CreateSalesOrder(
            salesOrder_id=uuid.uuid4(),
            salesOrder_number=SalesOrderNumber(create_sales_order_contract.SalesOrderNumber),
            customer_id=CustomerId(create_sales_order_contract.CustomerId),
            customer_name=CustomerName(create_sales_order_contract.CustomerName),
        )
        mediator = build_sales_mediator()
        mediator.send(create_sales_order)
