from fastapi import APIRouter 
from DataAccess.index import PostDA
from Models.index import Post
post_rt = APIRouter(tags=['post'])

@post_rt.get("/api/post/get-all")
async def get_all():
    return await PostDA.get_all_post()

@post_rt.get("/api/post/get-post-by-id/{id}")
async def get_by_id(id:str):
    return await PostDA.get_get_post_by_id(id)

@post_rt.post("/api/post/create-post")
async def create(post:Post):
    return await PostDA.create_post(post)

@post_rt.put("/api/post/update/{id}")
async def update(post:Post,id:str):
    return await PostDA.update_post(post,id)

@post_rt.put("/api/post/like/{id}")
async def like(id:str):
    return await PostDA.like_post(id)

@post_rt.put("/api/post/dislike/{id}")
async def dislike(id:str):
    return await PostDA.dislike_post(id)


@post_rt.delete("/api/post/delete/{id}")
async def delete(id:str):
    return await PostDA.delete_post(id)


