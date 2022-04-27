from Helper.DataHelper import DataHelper
from env.DatabaseConfig import db
from Models.index import Hotel
from bson import ObjectId

col_hotel = db.Hotels

class HotelDA:
    async def get_all_hotel():
        rs = []
        async for item in col_hotel.find():
            rs.append(DataHelper.hotel_convert(item))
        return rs
    
    async def get_hotel_by_id(id:str):
        res = await col_hotel.find_one({"_id":ObjectId(id)})
        return DataHelper.hotel_convert(res)
    
    async def create_hotel(hotel: Hotel):
        try:
            await col_hotel.insert_one(hotel.dict())
            return {"success" :  1}
        except: return {"success" :  -1}
    
    async def update_hotel(hotel: Hotel, id:str):
        try:
            async for item in col_hotel.find():
                if str(item['_id']) == id:
                    await col_hotel.update_one({"_id":ObjectId(id)},{
                        "$set":hotel.dict()
                    })
                    return {"success" : 1}
        except: return {"success" : -1}
    
    async def delete_hotel(id:str):
        try:
            await col_hotel.delete_one({"_id":ObjectId(id)})
            return {"success" : 1}
        except: return {"success" : -1}
    
    