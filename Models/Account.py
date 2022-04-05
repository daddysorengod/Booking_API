from pydantic import BaseModel

class Account(BaseModel):
    username : str
    password : str
    name : str
    email : str
    sex : str
    address : str
    national : str 
    avatar : str 
    createAt : str
    role : str
