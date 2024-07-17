from diator.events import DomainEvent, NotificationEvent
from diator.requests import Request


class BaseServiceBus:
    def send(self, command: Request) -> None:
        pass

    def publish(self, event: DomainEvent | NotificationEvent) -> None:
        pass
