import datetime

from pydantic import BaseModel


class CreateSalesOrderRowContract(BaseModel):
    BeerId: str
    BeerName: str
    Quantity: int


class CreateSalesOrderContract(BaseModel):
    SalesOrderNumber: str
    CustomerId: str
    CustomerName: str
    OrderDatetime: datetime.date
    SalesOrderRows: list[CreateSalesOrderRowContract]
