import uuid

from diator.events import DomainEvent
from diator.requests import Request, RequestHandler

from src.L50_Modules.Sales.Domain.CommandHandlers.CreateSalesOrderCommandHandler import CreateSalesOrderCommandHandler
from src.L50_Modules.Sales.Domain.Tests.BaseTest import BaseTest
from src.L50_Modules.Sales.Messages.Commands.CreateSalesOrder import CreateSalesOrder
from src.L50_Modules.Sales.Messages.Events.SalesOrderCreated import SalesOrderCreatedV2


class TestCreateSalesOrder(BaseTest):
    sales_order_id = uuid.uuid4()
    sales_order_number = "123"
    customer_id = uuid.uuid4()
    customer_name = "Pippo"

    def given(self):
        return []

    def when(self) -> Request:
        return CreateSalesOrder(
            salesOrder_id=self.sales_order_id,
            salesOrder_number=self.sales_order_number,
            customer_id=self.customer_id,
            customer_name=self.customer_name,
        )

    def on_handler(self, command: Request) -> RequestHandler[CreateSalesOrder, None]:
        return CreateSalesOrderCommandHandler(repository=self.repository)

    def then(self) -> list[DomainEvent]:
        return [
            SalesOrderCreatedV2(
                salesOrder_id=self.sales_order_id,
                salesOrder_number=self.sales_order_number,
                salesOrder_state="open",
                customer_id=self.customer_id,
                customer_name=self.customer_name,
            )
        ]


def test_create_sales_order():
    TestCreateSalesOrder().startup_test()
