from typing import Optional
from pydantic import BaseModel


class Image(BaseModel):
    _id : Optional[str] = None
    url: Optional[str] = None
    name:Optional[str] = None 