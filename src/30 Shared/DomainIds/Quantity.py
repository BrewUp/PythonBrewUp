from dataclasses import dataclass

@dataclass
class Quantity:
  def __init__(self, Value: float, UnitOfMeasure: str):
    self.Value = Value
    self.UnitOdMeasure = UnitOfMeasure