# import asyncio

from fastapi import FastAPI

from .endpoints import router

app = FastAPI()

app.include_router(router)


# async def startup():
#     pass


# if __name__ == "__main__":
#     asyncio.run(startup())
