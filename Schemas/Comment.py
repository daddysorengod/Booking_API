from pydantic import BaseModel

class Comment(BaseModel):
    id : str 
    idAccount : str
    content : str 
    idPost : str 
    likeCount : int 
    repId : str  
    