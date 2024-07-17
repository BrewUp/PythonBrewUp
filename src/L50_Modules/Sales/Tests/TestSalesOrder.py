import uuid
from unittest import mock

from src.L50_Modules.Sales.Domain.Entities.SalesOrder import SalesOrder
from src.L50_Modules.Sales.Messages.Events.SalesOrderClosed import SalesOrderClosed
from src.L50_Modules.Sales.Messages.Events.SalesOrderCreated import SalesOrderCreated, SalesOrderCreatedV2


def test_apply_on_SalesOrderCreated():
    sales_order = SalesOrder()
    sales_order_created = SalesOrderCreated(customer_name="pippo")
    sales_order.apply(sales_order_created)
    assert sales_order.salesOrder_id == sales_order.salesOrder_id
    assert sales_order.salesOrder_number == sales_order.salesOrder_number
    assert sales_order.salesOrder_state == "open"
    assert sales_order.customer_id == sales_order.customer_id
    assert sales_order.customer_name == sales_order.customer_name


def test_apply_on_SalesOrderCreatedV2():
    sales_order = SalesOrder()
    sales_order_created = SalesOrderCreatedV2(customer_name="pippo")
    sales_order.apply(sales_order_created)
    assert sales_order.salesOrder_id == sales_order_created.salesOrder_id
    assert sales_order.salesOrder_number == sales_order_created.salesOrder_number
    assert sales_order.salesOrder_state == "open"
    assert sales_order.customer_id == sales_order_created.customer_id
    assert sales_order.customer_name == sales_order_created.customer_name


def test_apply_on_SalesOrderClosed():
    sales_order = SalesOrder()
    sales_order_closed = SalesOrderClosed()
    sales_order.apply(sales_order_closed)
    assert sales_order.salesOrder_id == sales_order_closed.salesOrder_id
    assert sales_order.salesOrder_state == sales_order_closed.salesOrder_state


def test_apply_all_events():
    sales_order_id = uuid.uuid4()
    sales_order_created = SalesOrderCreated(salesOrder_id=sales_order_id, customer_name="pippo")
    sales_order_created_v2 = SalesOrderCreatedV2(salesOrder_id=sales_order_id, customer_name="pluto")
    sales_order_closed = SalesOrderClosed(salesOrder_id=sales_order_id)
    sales_order = SalesOrder(committed_events=[sales_order_created, sales_order_created_v2, sales_order_closed])
    sales_order.apply_committed_events()
    assert sales_order.salesOrder_id == sales_order_id
    assert sales_order.salesOrder_number == sales_order_created_v2.salesOrder_number
    assert sales_order.salesOrder_state == sales_order_closed.salesOrder_state
    assert sales_order.customer_id == sales_order_created_v2.customer_id
    assert sales_order.customer_name == "pluto"
