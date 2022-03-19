from pydantic import BaseModel
from typing import List
from Schemas import Comment

class Post(BaseModel):
    id : str 
    title : str
    content : str 
    picture : str 
    createAt : str 
    likeCount : int
    idComment : str 
    # comments : List[Comment] 