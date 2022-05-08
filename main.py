from fastapi import FastAPI
from env.DatabaseConfig import db
from Routers.index import (history_rt,account_rt,login_rt, room_rt, post_rt, comment_rt, hotel_rt,detail_rt)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account_rt)
app.include_router(login_rt)
app.include_router(room_rt)
app.include_router(post_rt)
app.include_router(comment_rt)
app.include_router(hotel_rt)
app.include_router(detail_rt)
app.include_router(history_rt)