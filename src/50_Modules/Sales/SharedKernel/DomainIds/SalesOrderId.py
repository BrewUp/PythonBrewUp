# import uuid
# SalesOrderId = uuid.UUID

from typing import NewType
import uuid

SalesOrderId = NewType('SalesOrderId', uuid.UUID)