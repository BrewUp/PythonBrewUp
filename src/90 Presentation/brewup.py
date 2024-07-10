from fastapi import FastAPI
from endpoints import handlegetdata, handlewelcomeonbrewup
import os

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

@app.get("/")
async def handleLandingPage():
  return await handlewelcomeonbrewup()
@app.get("/data/")
async def handleData(name: str):
  return await handlegetdata(name)

def main():
  os.system('uvicorn brewup:app --reload')

if __name__ == "__main__":
    main()