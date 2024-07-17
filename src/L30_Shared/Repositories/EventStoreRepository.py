from src.L30_Shared.CustomTypes.AggregateRoot import AggregateRoot
from src.L30_Shared.DomainIds.DomainId import DomainId


class EventStoreRepository:
    def get_by_id(self, domain_id: DomainId) -> AggregateRoot:
        pass

    def save(self, aggregate_root: AggregateRoot):
        pass
