from datetime import datetime
from Models.index import Account
from env.DatabaseConfig import db
from DatabaseHelper.DataHelper import account_helper
from Authentication.JwtAuth import AuthHandler

col_accounts = db.Accounts

auth_jwt = AuthHandler()

class AccountDA():
    async def create(account: Account):
            # account.password = auth_jwt.get_password_hash(account.password)
            # account.createAt = datetime.now()
            # new_account =  await col_accounts.insert_one(account.dict())
            # await col_accounts.find_one({"_id":new_account.inserted_id})
            # return 1
        
        return

    async def getAll():
        rs = []
        try:
            async for item in col_accounts.find():
                item["_id"] = str(item["_id"])
                rs.append(item)
            return rs
        except: 
            return rs
    
    async def update(id:int,account: Account):
        try: 
            async for item in col_accounts.find():
                if str(item['_id']) == id:
                    await col_accounts.update_one({"_id":item['_id']}, account)
                    return 1
        except:
            return -1
        
    async def delete(id:str):
        try: 
            async for item in col_accounts.find():
                if str(item['_id']) == id:
                    await col_accounts.delete_one({"_id":item['_id']})
                    return 1
        except:
            return -1
        
        