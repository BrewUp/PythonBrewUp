import uuid

from diator.events import DomainEvent
from diator.requests import Request, RequestHandler

from src.L30_Shared.Repositories.InMemoryRepository import InMemoryRepository
from src.L50_Modules.Sales.Domain.CommandHandlers.CreateSalesOrderCommandHandler import CreateSalesOrderCommandHandler
from src.L50_Modules.Sales.Domain.Tests.BaseTest import BaseTest
from src.L50_Modules.Sales.Messages.Commands.CreateSalesOrder import CreateSalesOrder
from src.L50_Modules.Sales.Messages.Events.SalesOrderCreated import SalesOrderCreated, SalesOrderCreatedV2


class TestCreateSalesOrder(BaseTest):
    sales_order_id = uuid.uuid4()
    sales_order_number = "123"
    customer_id = uuid.uuid4()
    customer_name = "Pippo"

    def given(self) -> list[DomainEvent]:
        return []

    def when(self) -> Request:
        return CreateSalesOrder(
            salesOrder_id=self.sales_order_id,
            salesOrder_number=self.sales_order_number,
            customer_id=self.customer_id,
            customer_name=self.customer_name,
        )

    def on_handler(self, command: Request) -> RequestHandler[CreateSalesOrder, None]:
        return CreateSalesOrderCommandHandler(command, repository=self.repository)

    def then(self)-> list[DomainEvent]:
        event_expected = SalesOrderCreated(
            salesOrder_id=self.sales_order_id,
            salesOrder_number=self.sales_order_number,
            customer_id=self.customer_id,
            customer_name=self.customer_name,
        )
        return [event_expected]


def test_create_sales_order(self):
    self.test_startup()
