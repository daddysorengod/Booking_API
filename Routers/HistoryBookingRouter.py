from fastapi import APIRouter

from DataAccess.index import HistoryBookingDA

history_rt = APIRouter(tags=["History Booking"])

@history_rt.get("/api/history/get-all")
async def get_all():
    return await HistoryBookingDA.get_all_history()
