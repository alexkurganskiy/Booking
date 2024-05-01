from typing import Optional
from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.hotels.models import Hotels
from app.bookings.models import Bookings
from app.database import Base


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]

    hotel: Mapped[Hotels] = relationship(back_populates="rooms")
    booking: Mapped[list["Bookings"]] = relationship(back_populates="rooms")

    def __str__(self):
        return f"Room {self.name}"