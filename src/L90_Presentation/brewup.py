import asyncio

from fastapi import FastAPI

from src.L50_Modules.Sales.Facade.SalesEndpoints import router as sales_router
from src.L50_Modules.Sales.Facade.SalesHelper import build_sales_mediator

from .endpoints import router

app = FastAPI()


async def main() -> None:
    build_sales_mediator()
    app.include_router(router)
    app.include_router(sales_router)


if __name__ == "__main__":
    asyncio.run(main())
