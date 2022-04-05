from pydantic import BaseModel

class Vourcher(BaseModel):
    code : str 
    name : str 
    discription : str 
    