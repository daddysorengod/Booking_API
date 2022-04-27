from typing import List, Optional 
from pydantic import BaseModel
from Models.Image import Image 

class Post(BaseModel):
    title : str
    content : str 
    createAt : str 
    likeCount : Optional[int] = 0
    idComment : str 
    image: List[Image] = None
    
    # comments : List[Comment] 