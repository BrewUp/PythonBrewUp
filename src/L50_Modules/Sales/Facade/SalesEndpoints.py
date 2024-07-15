from fastapi import APIRouter, status

from ..Facade import SalesFacade
from ..SharedKernel.Contracts.CreateSalesOrderContract import CreateSalesOrderContract

router = APIRouter()


@router.get("/sales/")
async def handlewelcomeonsales():
    return "Welcome to BrewUp API Sales Module"


@router.post("/sales/", status_code=status.HTTP_201_CREATED)
async def create_sales_order(request_payload: CreateSalesOrderContract):
    SalesFacade().create_sales_order(create_sales_order_contract=request_payload)
    return {"message": "ok"}
