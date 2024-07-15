from typing import NewType

from ..DomainIds.DomainId import DomainId

CustomerId = NewType("CustomerId", DomainId)
