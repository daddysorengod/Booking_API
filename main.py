from fastapi import FastAPI
from env.DatabaseConfig import db
from Routers.index import (account_rt,login_rt, room_rt, post_rt, comment_rt)

app = FastAPI()

app.include_router(account_rt)
app.include_router(login_rt)
app.include_router(room_rt)
app.include_router(post_rt)
app.include_router(comment_rt)
