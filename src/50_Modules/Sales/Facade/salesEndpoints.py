from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

@app.get("/")
async def handleSalesLandingPage():
  return await handleWelcomeOnSalesBoudedContext()

async def handleWelcomeOnSalesBoudedContext():
    return {"message": f"You are in Sales BoundedContext"}

