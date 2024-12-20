from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class VehicleType(Base):
    __tablename__="vehicle_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    body_types: Mapped[list["BodyType"]] = relationship(back_populates="vehicle_type")
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="vehicle_type")
    
