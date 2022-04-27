from typing import Optional, List
from pydantic import BaseModel
from Models.Image import Image


class Room(BaseModel):
    _id : Optional[str] = None
    roomCode : str 
    roomClass : str 
    state : Optional[str] = None
    price : Optional[str] = None 
    numberOfPeople: str
    checkIn: Optional[str] = None
    checkOut: Optional[str] = None
    hotelId:str
    image: List[Image] = None
