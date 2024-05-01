from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class Shotel(BaseModel):
    adress: str
    name: str 
    stars: int 

@app.get("/hotels", response_model=list[Shotel])
async def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5),
):  
    
    hotels = [
        {
            "address": "baker street 104",
            "name": "super hotel",
            "stars": 5,
        }
    ]
    
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.post("/bookings")
def add_booking(booking: SBooking):
    pass