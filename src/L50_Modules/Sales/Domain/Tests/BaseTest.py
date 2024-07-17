from diator.events import DomainEvent
from diator.requests import Request, RequestHandler

from src.L30_Shared.Repositories.InMemoryRepository import InMemoryRepository


class BaseTest:

    def __init__(self):
        self.repository = InMemoryRepository()
        pass

    def test_startup(self) -> None:
        self.repository.apply_given_events(self.given())
        handler = self.on_handler(self)
        handler.handle(self.when())
        expected = self.then()
        published = self.repository.events
        self.compare_events(expected, published)

    def given(self) -> list[DomainEvent]:
        pass

    def when(self) -> Request:
        pass

    def on_handler(self, command: Request) -> RequestHandler[Request, None]:
        pass

    def then(self) -> list[DomainEvent]:
        pass

    def compare_events(self, expected: list[DomainEvent], published: list[DomainEvent]) -> bool:
        return expected == published
