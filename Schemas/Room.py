from pydantic import BaseModel


class Room(BaseModel):
    id: str 
    roomCode : str 
    roomClass : str 
    state : str
    price : str 
    