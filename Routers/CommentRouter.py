from fastapi import APIRouter, Form
from Models.index import Comment
from DataAccess.index import CommentDA

comment_rt = APIRouter(tags=["comment"])

@comment_rt.post("/api/comments/create")
async def create(comment: Comment):
    return await CommentDA.create_comment(comment)

@comment_rt.get("/api/comments/get-commemt-post/{id}")
async def get_commemt_post(id:str):
    return await CommentDA.get_comment_by_id_post(id)

@comment_rt.get("/api/comments/get-comment-id/{id}")
async def get_comment_by_id(id:str):
    return await CommentDA.get_comment_by_id(id)

@comment_rt.put("/api/comments/update-comment/{id}")
async def update(id:str,comment:str = Form(...)):
    return await CommentDA.update_comment(id, comment)

@comment_rt.get("/api/comments")
async def get_all():
    return await CommentDA.get_all_comment()

@comment_rt.delete("/api/comments/delete/{id}")
async def delete(id:str):
    return await CommentDA.delete_comment(id)

@comment_rt.put("/api/comments/like/{id}")
async def like(id:str):
    return await CommentDA.like_comment(id)

@comment_rt.put("/api/comments/dislike/{id}")
async def like_dislike(id:str):
    return await CommentDA.dislike_comment(id)