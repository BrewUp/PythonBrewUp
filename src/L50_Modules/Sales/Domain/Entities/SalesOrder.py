import uuid
from dataclasses import dataclass, field
from functools import singledispatchmethod

from diator.events import DomainEvent

from src.L30_Shared.CustomTypes.AggregateRoot import AggregateRoot
from src.L30_Shared.DomainIds.CustomerId import CustomerId
from src.L30_Shared.DomainIds.CustomerName import CustomerName
from src.L50_Modules.Sales.Messages.Events.SalesOrderClosed import SalesOrderClosed
from src.L50_Modules.Sales.Messages.Events.SalesOrderCreated import SalesOrderCreated, SalesOrderCreatedV2
from src.L50_Modules.Sales.SharedKernel.CustomTypes import SalesOrderNumber
from src.L50_Modules.Sales.SharedKernel.DomainIds import SalesOrderId


@dataclass
class SalesOrder(AggregateRoot):
    salesOrder_id: SalesOrderId = field(default=uuid.uuid4())
    salesOrder_number: SalesOrderNumber = field(default="")
    salesOrder_state: str = field(default="open")
    customer_id: CustomerId = field(default=uuid.uuid4())
    customer_name: CustomerName = field(default="")

    apply = singledispatchmethod(AggregateRoot.apply)

    @staticmethod
    def create_sales_order(
        salesOrder_id: SalesOrderId,
        salesOrder_number: SalesOrderNumber,
        customer_id: CustomerId,
        customer_name: CustomerName,
    ):
        sales_order = SalesOrder(
            salesOrder_id=salesOrder_id,
            salesOrder_number=salesOrder_number,
            customer_id=customer_id,
            customer_name=customer_name,
        )
        sales_order._create_sales_order_v2()
        return sales_order

    def _create_sales_order(self):
        event = SalesOrderCreated(
            salesOrder_id=self.salesOrder_id,
            salesOrder_number=self.salesOrder_number,
            customer_id=self.customer_id,
            customer_name=self.customer_name,
        )
        self.raise_event(event)

    def _create_sales_order_v2(self):
        event = SalesOrderCreatedV2(
            salesOrder_id=self.salesOrder_id,
            salesOrder_number=self.salesOrder_number,
            salesOrder_state=self.salesOrder_state,
            customer_id=self.customer_id,
            customer_name=self.customer_name,
        )
        self.raise_event(event)

    def close_sales_order(self, salesOrder_id: SalesOrderId):
        event = SalesOrderClosed(salesOrder_id=salesOrder_id, salesOrder_state="closed")
        self.raise_event(event)

    @apply.register
    def _apply(self, event: SalesOrderCreated):
        sales_order_created_v2 = SalesOrderCreatedV2(
            salesOrder_id=event.salesOrder_id,
            salesOrder_number=event.salesOrder_number,
            salesOrder_state="open",
            customer_id=event.customer_id,
            customer_name=event.customer_name,
        )
        self.apply(sales_order_created_v2)

    @apply.register
    def _apply(self, event: SalesOrderCreatedV2):
        self.salesOrder_id = event.salesOrder_id
        self.salesOrder_number = event.salesOrder_number
        self.salesOrder_state = event.salesOrder_state
        self.customer_id = event.customer_id
        self.customer_name = event.customer_name

    @apply.register
    def _apply(self, event: SalesOrderClosed):
        self.salesOrder_id = event.salesOrder_id
        self.salesOrder_state = event.salesOrder_state
