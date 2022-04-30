from typing import List, Optional 
from pydantic import BaseModel
from Models.Image import Image 

class Post(BaseModel):
    _id : Optional[str] = None
    idHotel: Optional[str] = None
    title : Optional[str] = None
    content : Optional[str] = None 
    createAt : Optional[str] = None 
    likeCount : Optional[int] = 0
    idComment : Optional[str] = None 
    image: List[Image] = None
    