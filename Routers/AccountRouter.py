from fastapi import APIRouter
from Models.index import Account
from DataAccess.index import AccountDA
from fastapi.encoders import jsonable_encoder

account_rt = APIRouter()

@account_rt.get('/api/account')
async def getAllAccount():
    return await AccountDA.getAll()

@account_rt.post("/api/account")
async def addAccount(account: Account):
    new_account = await AccountDA.create(account)
    return new_account
