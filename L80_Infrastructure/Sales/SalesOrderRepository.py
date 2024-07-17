import json

from esdbclient import EventStoreDBClient

from src.L30_Shared.Repositories.EventStoreRepository import EventStoreRepository
from src.L50_Modules.Sales.Domain.Entities.SalesOrder import SalesOrder
from src.L50_Modules.Sales.SharedKernel.DomainIds.SalesOrderId import SalesOrderId


class SalesOrderRepository(EventStoreRepository):
    def __init__(self) -> None:
        self.client = EventStoreDBClient(
            uri="esdb://127.0.0.1:2113?Tls=false",
        )
        super().__init__()

    def get_by_id(self, sales_order_id: SalesOrderId) -> SalesOrder:
        streams = self.client.get_stream(stream_name=sales_order_id)
        sales_order = SalesOrder()
        for stream in streams:
            # TODO deserializza in un evento Event come SalesOrderCreated ecc..
            sales_order.apply(event=json.loads(stream))
        return sales_order

    def save(self, sales_order: SalesOrder):
        pass
