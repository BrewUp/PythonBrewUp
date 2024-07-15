from fastapi import APIRouter

from ..Facade import SalesFacade
from ..SharedKernel.Contracts import CreateSalesOrderContract

router = APIRouter()


@router.get("/sales/")
async def handlewelcomeonsales():
    return "Welcome to BrewUp API Sales Module"


@router.post("/sales/")
async def create_sales_order(request_payload: CreateSalesOrderContract):
    SalesFacade().create_sales_order(create_sales_order_contract=request_payload)
    return "ok"
