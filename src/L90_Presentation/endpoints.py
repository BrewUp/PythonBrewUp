from fastapi import APIRouter

router = APIRouter()


@router.get("/sales/")
async def handlewelcomeonsales():
    return "Welcome to BrewUp API Sales Module"


@router.get("/warehouses/")
async def handlewelcomeonwarehouses():
    return "Welcome to BrewUp API Warehouses Module"
