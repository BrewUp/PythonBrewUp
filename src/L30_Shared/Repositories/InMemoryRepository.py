from functools import singledispatchmethod

from diator.events import DomainEvent

from src.L30_Shared.CustomTypes.AggregateRoot import AggregateRoot
from src.L30_Shared.DomainIds.DomainId import DomainId
from src.L30_Shared.Repositories.Repository import Repository
from src.L50_Modules.Sales.Domain.Entities.SalesOrder import SalesOrder


class InMemoryRepository(Repository):
    def __init__(self) -> None:
        self.given_events: list[DomainEvent] = []
        self.events: list[DomainEvent] = []
        super().__init__()

    def apply_given_events(self, events: list[DomainEvent]):
        self.given_events = events

    def save(self, sales_order: SalesOrder):
        for event in sales_order.uncommited_events:
            self.events.append(event)
