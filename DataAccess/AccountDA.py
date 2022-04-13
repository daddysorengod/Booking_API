from datetime import datetime
import jwt
from Helper.DataHelper import DataHelper
from Models.index import Account
from env.DatabaseConfig import db
from Authentication.JwtAuth import AuthHandler
from bson import ObjectId

col_accounts = db.Accounts

auth_jwt = AuthHandler()

class AccountDA():
    
    # def check_account(email:str, username:str ) -> bool:
    #     x = col_accounts.find({"email":email})
    #     y = col_accounts.find({"usernmae":username})
    #     if x is None and y is None:
    #         return True
    #     else: return False 
    async def getAll(): 
        rs = []
        async for item in col_accounts.find():
            rs.append(DataHelper.account_convert(item))
        return rs 
    
    async def create(account: Account):
        
        #check email and username 
        con_username = await col_accounts.find_one({"username":account.username})
        con_email = await col_accounts.find_one({"email":account.email})
        if  con_email is not None or con_username is not None:
            check = False
        else:
            check = True
            
            
        if check == True:
            try: 
                account.password = auth_jwt.get_password_hash(account.password)
                account.createAt = datetime.now()
                account.token = ""
                new_account =  await col_accounts.insert_one(account.dict())
                await col_accounts.find_one({"_id":new_account.inserted_id})
                return 1
            except:   
                return -1
        else: return -2
            
    async def get_user_by_id(id:str):
        rep = await col_accounts.find_one({"_id":ObjectId(id)})
        return DataHelper.account_convert(rep)
    
    
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
        
    