from datetime import datetime

import jwt
from Models.index import Account
from env.DatabaseConfig import db
from DatabaseHelper.DataHelper import account_helper
from Authentication.JwtAuth import AuthHandler
from bson import ObjectId

col_accounts = db.Accounts

auth_jwt = AuthHandler()

class AccountDA():
    async def create(account: Account):
        try: 
            account.password = auth_jwt.get_password_hash(account.password)
            account.createAt = datetime.now()
            account.token = ""
            new_account =  await col_accounts.insert_one(account.dict())
            await col_accounts.find_one({"_id":new_account.inserted_id})
            return 1
        except:   
            return -1

    async def getAll():
        rs = []
        try:
            async for item in col_accounts.find():
                item["_id"] = str(item["_id"])
                rs.append(item)
            return rs
        except: 
            return rs
    
    async def update_password(id:int,new_password: str):
        try: 
            async for item in col_accounts.find():
                if str(item['_id']) == id:
                    await col_accounts.update_one({"_id":ObjectId(id)},{"$set":{"password":auth_jwt.get_password_hash(new_password)}})
                    return 1
        except:
            return -1
        
    async def delete(id:str):
        try: 
            account = await col_accounts.find_one({"_id": ObjectId(id)})
            if account:
                await col_accounts.delete_one({"_id":ObjectId(id)})
                return 1
        except:
            return -1
        
        