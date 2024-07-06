from fastapi import FastAPI
from endpoints import handleGetData
import os

app = FastAPI()

@app.get("/data/")
async def handleData():
  return await handleGetData()

def main():
  os.system('uvicorn brewup:app --reload')

if __name__ == "__main__":
    main()