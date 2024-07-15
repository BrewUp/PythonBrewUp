async def handlewelcomeonbrewup():
    return "Welcome to BrewUp API"

async def handlegetdata(name: str):
    return {"message": f"Hello {name}"}
