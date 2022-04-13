from pydantic import BaseModel


class Room(BaseModel):
    roomCode : str 
    roomClass : str 
    state : str
    price : str 
    numberOfPeople: str
    checkIn: str
    checkOut: str
