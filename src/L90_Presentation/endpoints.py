from brewup import app


@app.get("/sales/")
async def handlewelcomeonsales():
    return "Welcome to BrewUp API Sales Module"


@app.get("/warehouses/")
async def handlewelcomeonwarehouses():
    return "Welcome to BrewUp API Warehouses Module"
