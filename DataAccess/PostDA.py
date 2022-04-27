from Models.index import Post
from env.DatabaseConfig import db
from bson import ObjectId
from Helper.DataHelper import DataHelper
from datetime import datetime

col_post = db.Posts

class PostDA:
    async def create_post(post:Post):
        try:
            post.createAt = datetime.now()
            await col_post.insert_one(post.dict())
            return {"success" :  1}
        except: 
            return {"success" :  -1}

    async def update_post(post:Post, id:str):
        try: 
            await col_post.update_one({"_id":ObjectId(id)},{"$set": post.dict()})
            return {"success" :  1}
        except: return {"success" :  -1}
        
    async def get_all_post():
        rs = []
        async for item in col_post.find():
            rs.append(DataHelper.post_convert(item))
        return rs
            
    async def get_get_post_by_id(id:str):
        res = await col_post.find_one({'_id':ObjectId(id)})        
        return DataHelper.post_convert(res)
    
    async def delete_post(id:str):
        try:
            await col_post.delete_one({"_id":ObjectId(id)})
            return {"success" :  1}
        except : return {"success" :  -1}
        
    async def like_post(id:str):
        data = await PostDA.get_get_post_by_id(id)
        try: 
            await col_post.update_one({"_id":ObjectId(id)},{
                "$set":{
                    "likeCount":data['likeCount']+1
                }
            })
            return {"success" :  1}
        except: return {"success" :  -1}
    
    async def dislike_post(id:str):
        data = await PostDA.get_get_post_by_id(id)
        try: 
            await col_post.update_one({"_id":ObjectId(id)},{
                "$set":{
                    "likeCount":data['likeCount']-1
                }
            })
            return {"success" :  1}
        except: return {"success" :  -1}
        
    async def update_idComment(id:str, idComment:str):
        try:
            await col_post.update_one({"_id":ObjectId(id)},{
                "$set": {
                    "idComment": idComment
                }
            })
            return {"success" :  1}
        except: return {"success" :  -1}