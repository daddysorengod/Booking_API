from pydantic import BaseModel
from typing import List, Optional 
from Models.Image import Image 

class Hotel(BaseModel): 
    nameHotel: str
    star : int
    location : str
    description: str
    image : List[Image] = None
    # idComment : Optional[str]
