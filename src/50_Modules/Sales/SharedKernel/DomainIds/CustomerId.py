# class CustomerId:
#   def __init__(self, Value):
#     self.Value = Value

#   def __str__(self):
#     return str(self.Value)

#   def __eq__(self, other):
#     if isinstance(other, CustomerId):
#       return self.Value == other.Value
#     return False

#   def __hash__(self):
#     return hash(self.Value)

from typing import NewType
import uuid

CustomerId = NewType('CustomerId', uuid.UUID)