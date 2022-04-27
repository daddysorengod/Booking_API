from pydantic import BaseModel
from typing import List, Optional 
from Models.Image import Image 

class Hotel(BaseModel): 
    _id : Optional[str] = None
    nameHotel: Optional[str] = None
    star : Optional[int] = 0
    location : Optional[str] = None
    description: Optional[str] = None
    image : List[Image] = None
    # idComment : Optional[str]
