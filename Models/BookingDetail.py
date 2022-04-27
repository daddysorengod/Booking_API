from typing import Optional, List
from pydantic import BaseModel
from Models.index import Room, Account


class BookingDetail(BaseModel):
    _id : Optional[str] = None
    checkIn: Optional[str] = None
    account:Account
    room : List[Room]
    staying: int
    state: Optional[str] = None
    totalPrice : Optional[str] = None
    