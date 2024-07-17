from diator.events import DomainEvent
from diator.requests import Request


class BaseTest:
    def given(self, committed_events: list[DomainEvent]):
        pass

    def when(self) -> Request:
        pass

    def on_handler(self, command: Request):
        pass

    def then(self):
        pass
