from datetime import datetime
from DataAccess.index import RoomDA
from env.DatabaseConfig import db
from Models.index import HistoryBooking
from bson import ObjectId
from Helper.DataHelper import DataHelper

col_history = db.HistoryBooking

class HistoryBookingDA():
    async def get_all_history():
        rs = []
        async for item in col_history.find():
            rs.append(DataHelper.history_convert(item))
        return rs
    
    async def get_history_by_id(id:str):
        res = await col_history.find_one({"_id":ObjectId(id)})
        return DataHelper.history_convert(res)
    
    async def create_history(history: HistoryBooking):
        try:
            await col_history.insert_one(history.dict())
            return {"success" :  1}
        except: return {"success" :  -1}
    
    # async def checkin_room(checkIn: str, id:str):
    #     try:
    #         async for item in col_history.find():
    #             if str(item['_id']) == id:
    #                 await col_history.update_one({"_id":ObjectId(id)},{
    #                     "$set":{
    #                         "checkIn": checkIn,
    #                     }
    #                 })
    #                 await RoomDA.update_room_state(item['room']['roomCode'],"unavalible")
    #                 return {"success" : 1}
    #     except: return {"success" :  -1}
    
    async def checkout_room(checkOut: str, id: str):
        try:
            async for item in col_history.find():
                if str(item['_id']) == id:
                    await col_history.update_one({"_id":ObjectId(id)},{
                        "$set":{
                            "checkIn": checkOut,
                        }
                    })
                    await RoomDA.update_room_state(item['room']['roomCode'],"avalible")
                    return {"success" : 1}
        except: return {"success" :  -1}
    