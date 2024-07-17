from unittest import mock

from src.L50_Modules.Sales.Domain.Entities.SalesOrder import SalesOrder
from src.L50_Modules.Sales.Messages.Events.SalesOrderClosed import SalesOrderClosed
from src.L50_Modules.Sales.Messages.Events.SalesOrderCreated import SalesOrderCreated


def test_apply_on_SalesOrderCreated():
    sales_order = SalesOrder()
    sales_order_created = SalesOrderCreated(customer_name="pippo")
    sales_order.apply(sales_order_created)
    assert sales_order.customer_name == "pippo"


def test_apply_on_SalesOrderClosed():
    sales_order = SalesOrder()
    sales_order_closed = SalesOrderClosed()
    sales_order.apply(sales_order_closed)
    assert sales_order.salesOrder_id == sales_order_closed.salesOrder_id


def test_apply_all_events():
    sales_order_created = SalesOrderCreated(customer_name="pippo")
    sales_order_closed = SalesOrderClosed()
    sales_order = SalesOrder(committed_events=[sales_order_created, sales_order_closed])
    sales_order.apply_committed_events()
    assert sales_order.customer_name == "pippo"
