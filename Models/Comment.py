from typing import Optional
from pydantic import BaseModel

class Comment(BaseModel):
    idAccount : str
    content : str 
    idPost : str 
    likeCount : Optional[int] = 0 
    
    