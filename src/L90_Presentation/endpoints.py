from fastapi import APIRouter

router = APIRouter()


@router.get("/warehouses/")
async def handlewelcomeonwarehouses():
    return "Welcome to BrewUp API Warehouses Module"
