from fastapi import APIRouter, Form
from DataAccess.index import BookingDetailDA,HistoryBookingDA
from Models.index import BookingDetail,HistoryBooking

detail_rt = APIRouter(tags=["booking detail"])

@detail_rt.get("/api/booking-detail/get-all")
async def get_all():
    return await BookingDetailDA.get_all_detail()

@detail_rt.get("/api/booking-detail/get-by-username/{username}")
async def get_by_username(username:str):
    return await BookingDetailDA.get_detail_by_username(username)

    
@detail_rt.get("/api/booking-detail/get-by-id/{id}")
async def get_by_id(id:str):
    return await BookingDetailDA.get_detail_by_id(id)

@detail_rt.post("/api/booking-detail/create")
async def create(detail: BookingDetail):
    # try:
    #     await BookingDetailDA.create_detail(detail)
    #     for item in detail.room: 
    #         history = HistoryBooking(room = item, checkIn=detail.checkIn)
    #         await HistoryBookingDA.create_history(history)   
    #     return {"success" :  1} 
    # except:
    #     return {"success" :  -1}
    return await BookingDetailDA.create_detail(detail)

@detail_rt.put("/api/booking-detail/confirm/{id}")
async def confirm(id:str):
    try:
        await BookingDetailDA.update_state_detail(id)
        res = await BookingDetailDA.get_detail_by_id(id)
        for item in res['room']:
            history = HistoryBooking(room = item, checkIn=res['checkIn'])
            await HistoryBookingDA.create_history(history)
        return {"success": 1}
    except: return {"success" :  -1}
