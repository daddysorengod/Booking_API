from ast import For
from fastapi import APIRouter,Form
from Models.index import Login
from env.DatabaseConfig import db
from Authentication.JwtAuth import AuthHandler
from Helper.DataHelper import DataHelper
from Helper.Mailhelper import send_mail

login_rt = APIRouter(tags=["login"])
col_account = db.Accounts
jwt_auth = AuthHandler()

@login_rt.post("/api/login-gen-token")
async def Login_Gen_Token(account:Login):
    rs = await col_account.find_one({"username":account.username})
    if rs:
        if jwt_auth.verify_password(account.password, rs['password']):
            token = jwt_auth.encode_token(str(rs['_id']))
            send_mail(rs['email'],token)
            query = {"username":account.username}
            value = {"$set":{"token":token}}
            col_account.update_one(query, value)
            return {
                "token": token
            }
        else: return -1
        
@login_rt.get("/api/login-verify-token")
async def Login_Verify_Token(token:str = Form(...)):
    rs = await col_account.find_one({"token":token})
    if rs:
        query = {"token":token}
        value = {"$set":{"token":""}}
        await col_account.update_one(query, value)
        return DataHelper.account_convert(rs)
    else: return -1 