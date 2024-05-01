from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from hotels.rooms.models import Rooms

    
class Hotels(Base): 
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    location: Mapped[str] = mapped_column()
    services: Mapped[dict] = mapped_column(JSON)
    rooms_quantitiy: Mapped[int] = mapped_column()
    image_id: Mapped[int] = mapped_column()

    rooms: Mapped[list["Rooms"]] = relationship(back_populates="hotel")