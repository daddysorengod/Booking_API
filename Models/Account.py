from typing import Optional
from pydantic import BaseModel

class Account(BaseModel):
    username : str
    password : str
    name : str
    email : str
    sex : Optional[str] = None
    address : str
    national : str 
    avatar : Optional[str] = None
    createAt : str
    hotelId: Optional[str] = None
    token: Optional[str] = None
    role : str
