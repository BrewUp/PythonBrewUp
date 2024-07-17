from diator.events import DomainEvent
from diator.requests import Request, RequestHandler

from src.L30_Shared.Repositories.InMemoryRepository import InMemoryRepository


class BaseTest:
    def startup_test(self) -> None:
        self.repository = InMemoryRepository()
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
        zipped_events = zip(expected, published)
        is_valid = len(expected) == len(published)
        for e, p in zipped_events:
            if not is_valid:
                break
            is_valid = type(e) == type(p) and e == p
        assert is_valid is True
