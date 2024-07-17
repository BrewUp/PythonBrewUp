import uuid

# from typing import NewType

# DomainId = NewType("DomainId", uuid.UUID)


class DomainId(uuid.UUID):
    pass
