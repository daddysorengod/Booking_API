from Helper.DataHelper import DataHelper
from Models.index import HistoryBooking
from env.DatabaseConfig import db
from Models.index import BookingDetail
from bson import ObjectId

col_detail = db.BookingDetail

class BookingDetailDA:
    async def get_all_detail():
        rs = []
        async for item in col_detail.find():
            rs.append(DataHelper.detail_convert(item))           
        return rs
    
    async def get_detail_by_id(id:str):
        res = await col_detail.find_one({"_id":ObjectId(id)})
        return DataHelper.detail_convert(res)
    
    async def get_detail_by_username(username:str):
        rs = []
        try: 
            async for item in col_detail.find():
                if item['account']['username'] == username:
                    rs.append(DataHelper.detail_convert(item))
            return rs          
        except: return rs
    
    async def create_detail(detail:BookingDetail):
        totalPrice = 0
        for item in detail.room:
            totalPrice = totalPrice + float(item.price * detail.staying)
        
        try:
            detail.totalPrice = str(totalPrice)
            detail.state = "pending"
            await col_detail.insert_one(detail.dict())            
            return {"success" :  1}
        except: return {"success" :  -1}
        
    async def update_detail(detail:BookingDetail, id:str):
        try:
            async for item in col_detail.find():
                if str(item['_id']) == id:
                    col_detail.update_one({"_id":ObjectId(id)},{
                        "$set":detail
                    })
                return {"success" :  1}
        except: return {"success" : -1}
        
    async def update_state_detail(id:str):
        try:
            async for item in col_detail.find():
                if str(item['_id']) == id:
                    col_detail.update_one({"_id":ObjectId(id)},{
                        "$set":{
                            "state":"done"
                        }
                    })
                return {"success" :  1}
        except: return {"success" : -1}
    
