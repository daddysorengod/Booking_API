from typing import Optional
from pydantic import BaseModel

class Comment(BaseModel):
    _id : Optional[str] = None
    idAccount : Optional[str] = None
    content : Optional[str] = None 
    idPost :Optional[str] = None
    likeCount : Optional[int] = 0 
    
    