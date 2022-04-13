from fastapi import APIRouter, Form
from Models.index import Account
from DataAccess.index import AccountDA
from fastapi.encoders import jsonable_encoder

account_rt = APIRouter(tags=["account"])

@account_rt.get('/api/account')
async def getAllAccount():
    return await AccountDA.getAll()

@account_rt.post("/api/account/create")
async def addAccount(account: Account):
    new_account = await AccountDA.create(account)
    return new_account

@account_rt.put("/api/account/update-password/{id}")
async def update(id:str, new_password:str = Form(...)):
    new_account = await AccountDA.update_password(id,new_password)
    return new_account

@account_rt.delete("/api/account/delete/{id}")
async def delete(id:str):
    new_account = await AccountDA.delete(id)
    return new_account

@account_rt.get("/api/account/get-by-id/{id}")
async def get_id(id:str):
    return await AccountDA.get_user_by_id(id)