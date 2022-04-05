from pydantic import BaseModel

class Post(BaseModel):
    title : str
    content : str 
    picture : str 
    createAt : str 
    likeCount : int
    idComment : str 
    # comments : List[Comment] 