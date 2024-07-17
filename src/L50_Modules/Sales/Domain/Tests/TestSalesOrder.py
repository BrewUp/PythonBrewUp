import uuid

from diator.events import DomainEvent
from diator.requests import Request

from src.L30_Shared.Repositories.InMemoryRepository import InMemoryRepository
from src.L50_Modules.Sales.Domain.CommandHandlers.CreateSalesOrderCommandHandler import CreateSalesOrderCommandHandler
from src.L50_Modules.Sales.Domain.Tests.BaseTest import BaseTest
from src.L50_Modules.Sales.Messages.Commands.CreateSalesOrder import CreateSalesOrder
from src.L50_Modules.Sales.Messages.Events.SalesOrderCreated import SalesOrderCreated


class TestCreateSalesOrder(BaseTest):
    sales_order_id = uuid.uuid4()
    sales_order_number = "123"
    customer_id = uuid.uuid4()
    customer_name = "Pippo"
    repository = InMemoryRepository()

    def given(self, given_events: list[DomainEvent]):
        pass

    def when(self) -> Request:
        return CreateSalesOrder(
            salesOrder_id=self.sales_order_id,
            salesOrder_number=self.sales_order_number,
            customer_id=self.customer_id,
            customer_name=self.customer_name,
        )

    def on_handler(self, command: Request):
        CreateSalesOrderCommandHandler(command, repository=self.repository)

    def then(self):
        event_expected = SalesOrderCreated(
            salesOrder_id=self.sales_order_id,
            salesOrder_number=self.sales_order_number,
            salesOrder_state="open",
            customer_id=self.customer_id,
            customer_name=self.customer_name,
        )
        assert event_expected == self.repository.events[0]


def test_create_sales_order():
    test_handler = TestCreateSalesOrder()
    test_handler.given([])
    create_sales_order = test_handler.when()
    test_handler.on_handler(create_sales_order)
    test_handler.then()
