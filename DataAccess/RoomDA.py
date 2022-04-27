from env.DatabaseConfig import db
from Helper.DataHelper import DataHelper
from Models.Room import Room
from bson import ObjectId

col_room = db.Rooms

class RoomDA:
    async def get_all_room():
        rs = []
        async for item in col_room.find():
            rs.append(DataHelper.room_convert(item))
        return rs

    async def create_room(room: Room):
        try:
            room.state = "avalible"
            await col_room.insert_one(room.dict())
            return {"success" :  1}
        except: 
            return {"success" :  -1}
        
    async def update_room_state(roomCode:str, state:str):
        try: 
            await col_room.update_one({"roomCode":roomCode},{
                "$set":{
                    "state":state
                }
            })
            return {"success" :  1}
        except: return {"success" :  -1}
        
    async def get_room_by_id(id:str):
        res = await col_room.find_one({"_id":ObjectId(id)})
        return DataHelper.room_convert(res)
        
    # async def update_room_check_in(roomCode:str, checkIn:str):
    #     try: 
    #         await col_room.update_one({"roomCode":roomCode},{
    #             "$set":{
    #                 "checkIn":checkIn
    #             }
    #         })
    #         return {"success" :  1}
    #     except: return {"success" :  -1}
        
    # async def update_room_check_out(roomCode:str, checkOut:str):
    #     try: 
    #         await col_room.update_one({"roomCode":roomCode},{
    #             "$set":{
    #                 "checkOut":checkOut
    #             }
    #         })
    #         return {"success" :  1}
    #     except: return {"success" :  -1}
        
    async def update_room_price(roomCode:str ,price:str):
        try: 
            await col_room.update_one({"roomCode":roomCode},{
                "$set":{
                    "price":price
                }
            })
            return {"success" :  1}
        except: return {"success" :  -1}
        
    async def delete_room(id:str):
        try: 
            await col_room.delete_one({"_id":ObjectId(id)})
            return {"success" :  1}
        except: return {"success" :  -1}