from fastapi import APIRouter
from DataAccess.index import HotelDA
from Models.index import Hotel
hotel_rt = APIRouter(tags=["hotel"])

@hotel_rt.get("/api/hotel/get-all")
async def get_all():
    return await HotelDA.get_all_hotel()

@hotel_rt.get("/api/hotel/get-by-id/{id}")
async def get_by_id(id:str):
    return await HotelDA.get_hotel_by_id(id)

@hotel_rt.post("/api/hotel/create")
async def create(hotel: Hotel):
    return await HotelDA.create_hotel(hotel)

@hotel_rt.put("/api/hotel/update/{id}")
async def update(hotel: Hotel, id:str):
    return await HotelDA.update_hotel(hotel, id)

@hotel_rt.delete("/api/hotel/delete/{id}")
async def delete(id:str):
    return await HotelDA.delete_hotel(id)