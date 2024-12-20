from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class BodyType(Base):
    __tablename__="body_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    vehicle_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("vehicle_types.id"), nullable=False)
    vehicle_type: Mapped["VehicleType"] = relationship(back_populates="body_types")
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="body_type")

