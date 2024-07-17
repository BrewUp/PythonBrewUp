from src.L30_Shared.CustomTypes.AggregateRoot import AggregateRoot
from src.L30_Shared.DomainIds.DomainId import DomainId


class Repository:
    def get_by_id(self, domain_id: DomainId) -> AggregateRoot:
        raise NotImplementedError

    def save(self, aggregate_root: AggregateRoot):
        raise NotImplementedError
