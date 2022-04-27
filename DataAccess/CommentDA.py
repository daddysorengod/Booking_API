import re
from Helper.DataHelper import DataHelper
from env.DatabaseConfig import db
from bson import ObjectId
from Models.index import Comment

col_comment = db.Comments

class CommentDA:
    async def create_comment(comment:Comment):
        try:
            await col_comment.insert_one(comment.dict())
            return {"success" :  1}
        except: return {"success" :  -1}
        
    async def update_comment(id:str, comment:str):
        try: 
            async for item in col_comment.find():
                if str(item['_id']) == id:
                    await col_comment.update_one({"_id":ObjectId(id)},{
                        "$set":{
                            "content":comment
                        }
                    })
                    return {"success" :  1}
        except: return {"success" :  -1}
        
    async def get_comment_by_id(id:str):
        rep = await col_comment.find_one({'_id':ObjectId(id)})
        return DataHelper.comment_convert(rep)
    
    async def get_comment_by_id_post(id:str):
        rs = []
        async for item in col_comment.find({"idPost":id}):
            rs.append(DataHelper.comment_convert(item))
        return rs
        
    
    async def delete_comment(id:str):
        try: 
            await col_comment.delete_one({"_id":ObjectId(id)})
            return {"success" :  1}
        except: return {"success" :  -1}
        
    async def get_all_comment():
        rs = []
        async for item in col_comment.find():
            rs.append(DataHelper.comment_convert(item))
        return rs
    
    async def like_comment(id:str):
        data = await CommentDA.get_comment_by_id(id)
        try:
            await col_comment.update_one({"_id":ObjectId(id)},{
                "$set":{
                    "likeCount": data["likeCount"]+1
                }
            })
            return {"success": 1}
        except: return {"success" :  -1}
        
    async def dislike_comment(id:str):
        data = await CommentDA.get_comment_by_id(id)
        try:
            await col_comment.update_one({"_id":ObjectId(id)},{
                "$set":{
                    "likeCount": data["likeCount"]-1
                }
            })
            return {"success": 1}
        except: return {"success" :  -1}