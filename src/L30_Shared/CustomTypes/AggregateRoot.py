from dataclasses import dataclass, field

from diator.events import DomainEvent


@dataclass
class AggregateRoot:
    uncommited_events: list[DomainEvent] = field(default_factory=list)
    committed_events: list[DomainEvent] = field(default_factory=list)
    version: int = field(default=0)

    def raise_event(self, event: DomainEvent):
        self.uncommited_events.append(event)

    def apply(self, event: DomainEvent):
        raise NotImplementedError

    def apply_committed_events(self):
        for event in self.committed_events:
            self.apply(event)
            self.version += 1
