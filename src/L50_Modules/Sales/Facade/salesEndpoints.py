from fastapi import FastAPI
from L30_Shared.DomainIds.BeerName import BeerName

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


@app.get("/")
async def handleSalesLandingPage():
    beerName1 = BeerName("IPA")
    beerName2 = BeerName("IPA")

    beerName1 == beerName2

    return await handleWelcomeOnSalesBoudedContext()


async def handleWelcomeOnSalesBoudedContext():
    return {"message": f"You are in Sales BoundedContext"}
