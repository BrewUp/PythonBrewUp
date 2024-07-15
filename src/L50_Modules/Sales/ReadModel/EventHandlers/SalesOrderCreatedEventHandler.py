import event
from diator.events import EventHandler

from ...Messages.Events import SalesOrderCreated


class SalesOrderCreatedEventHandler(EventHandler[SalesOrderCreated]):
    def __init__(self, meeting_api: MeetingAPI) -> None:
        self._meeting_api = meeting_api

    async def handle(self, event: SalesOrderCreated) -> None:
        await self._meeting_api.notify(event.meeting_id, "New user joined!")
