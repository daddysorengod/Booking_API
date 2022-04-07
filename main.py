from fastapi import FastAPI
from env.DatabaseConfig import db
from Routers.index import (account_rt,login_rt)

app = FastAPI()

app.include_router(account_rt)
app.include_router(login_rt)
