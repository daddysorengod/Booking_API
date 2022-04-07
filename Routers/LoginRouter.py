from ast import For
from fastapi import APIRouter,Form
from Models.index import Account
from env.DatabaseConfig import db
from Authentication.JwtAuth import AuthHandler

login_rt = APIRouter()
col_account = db.Accounts
jwt_auth = AuthHandler()

@login_rt.post("api/login-gen-token")
async def Login_Gen_Token(username:str = Form(...), password:str = Form(...)):
    rs = col_account.find_one({"username":username})
    if rs:
        if jwt_auth.verify_password(password, rs['password']):
            return rs
        else: return -1