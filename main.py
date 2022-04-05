from fastapi import FastAPI
from env.DatabaseConfig import db
from Routers.index import (account_rt)
import uvicorn

app = FastAPI()

app.include_router(account_rt)

# @app.get("/")
# async def getHello():
#     print(db.list_collection_names())]=[p0o9iuyjhtrgfdcz-09
#     return {"hello" : " world"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)