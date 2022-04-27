from typing import Optional
from pydantic import BaseModel

from Models.Room import Room


class HistoryBooking(BaseModel):
    _id : Optional[str] = None
    room: Room
    checkIn: Optional[str] = None
    checkOut: Optional[str] = None
    