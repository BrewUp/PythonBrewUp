from diator.events import DomainEvent

from src.L30_Shared.CustomTypes.AggregateRoot import AggregateRoot
from src.L30_Shared.DomainIds.DomainId import DomainId
from src.L30_Shared.Repositories.Repository import Repository


class InMemoryRepository(Repository):
    given_events: list[DomainEvent] = []
    events: list[DomainEvent] = []

    def apply_given_events(self, aggregate_root: AggregateRoot):
        for event in self.given_events:
            aggregate_root.apply(event)

    def save(self, aggregate_root: AggregateRoot):
        print("SONO QUI")
        for event in aggregate_root.committed_events:
            self.given_events.append(event)
