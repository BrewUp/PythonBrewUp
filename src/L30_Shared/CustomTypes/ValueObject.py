import dataclasses

@dataclasses.dataclass(frozen=True)
class ValueObject:
    pass

    def __eq__(self, value: object) -> bool:
        pass