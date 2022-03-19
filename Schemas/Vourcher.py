from pydantic import BaseModel

class Vourcher(BaseModel):
    id : str
    code : str 
    name : str 
    discription : str 
    