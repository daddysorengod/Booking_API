from pydantic import BaseModel

class Comment(BaseModel):
    idAccount : str
    content : str 
    idPost : str 
    likeCount : int 
    repId : str  
    