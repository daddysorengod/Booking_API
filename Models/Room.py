from typing import Optional
from pydantic import BaseModel


class Room(BaseModel):
    roomCode : str 
    roomClass : str 
    state : str
    price : str 
    numberOfPeople: str
    checkIn: Optional[str] = None
    checkOut: Optional[str] = None
    hotelId:str

