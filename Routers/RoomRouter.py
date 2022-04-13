from DataAccess.index import RoomDA
from fastapi import APIRouter,Form

from Models.index import Room

room_rt = APIRouter(tags=["room"])

@room_rt.get("/api/room/get-all")
async def get_all():
    return await RoomDA.get_all_room()

@room_rt.post("/api/room/create")
async def create(room:Room):
    return await RoomDA.create_room(room)


@room_rt.put("/api/room/update-room-state")
async def update_state(roomCode:str = Form(...), state:str = Form(...)):
    return await RoomDA.update_room_state(roomCode, state)

@room_rt.put("/api/room/update-room-checkin")
async def update_state(roomCode:str = Form(...), checkIn:str = Form(...)):
    return await RoomDA.update_room_check_in(roomCode, checkIn)

@room_rt.put("/api/room/update-room-checkout")
async def update_state(roomCode:str = Form(...), checkOut:str = Form(...)):
    return await RoomDA.update_room_check_out(roomCode, checkOut)

@room_rt.delete("/api/room/delete/{id}")
async def delete(id:str):
    return await RoomDA.delete_room(id)