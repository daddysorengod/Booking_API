from pydantic import BaseModel


class AccountDetail(BaseModel):
    id : str
    id_account : str
    name : str
    email : str
    national : str 
    avatar : str 
    createAt : str
    role : str