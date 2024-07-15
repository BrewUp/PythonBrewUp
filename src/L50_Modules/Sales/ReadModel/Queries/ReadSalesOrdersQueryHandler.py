from diator.requests import RequestHandler

from ...Messages.Queries.ReadSalesOrdersQuery import ReadSalesOrderQuery


class ReadSalesOrdersQueryHandler(
    RequestHandler[ReadSalesOrderQuery, ReadSalesOrderQueryResult]
):
    def __init__(self, sales_api: SalesApi) -> None:
        self._sales_api = sales_api
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: ReadSalesOrderQuery) -> ReadSalesOrderQueryResult:
        link = await self._sales_api.get_link(request.salesOrder_id)
        return ReadSalesOrderQueryResult(salesOrder_id=request.salesOrder_id, link=link)
