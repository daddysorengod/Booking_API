from typing import Optional
from pydantic import BaseModel

class Account(BaseModel):
    _id : Optional[str] = None
    username : Optional[str] = None
    password : Optional[str] = None
    name : Optional[str] = None
    email : Optional[str] = None
    sex : Optional[str] = None
    address : Optional[str] = None
    national : Optional[str] = None
    avatar : Optional[str] = None
    createAt : Optional[str] = None
    hotelId: Optional[str] = None
    token: Optional[str] = None
    role : Optional[str] = None
