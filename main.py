from fastapi import FastAPI
from env.DatabaseConfig import db

app = FastAPI()

@app.get("/")
async def getHello():
    print(db.list_collection_names())
    return {"hello" : " world"}
