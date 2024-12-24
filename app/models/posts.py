from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, String, Table, DateTime, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
import datetime

class Post(Base):
    __tablename__= "posts"

    # base post datas
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False, index=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, onupdate=func.now(), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


    # base vehicle datas
    year: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    mileage: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    engine_displacement: Mapped[float] = mapped_column(Numeric(precision=4, scale=1), nullable=False, index=True)
    kilowatts: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    horsepowers: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    color: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    # exclusive car vehicle attribute
    doors_number: Mapped[str] = mapped_column(String, nullable=True, index=True)
    # exclusive truck vehicle attributes
    payload_capacity: Mapped[str] = mapped_column(String, nullable=True, index=True)
    axle_count: Mapped[str] = mapped_column(String, nullable=True, index=True)


    # foreign keys
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    fuel_id: Mapped[int] = mapped_column(Integer, ForeignKey("fuels.id"), nullable=False)
    model_id: Mapped[int] = mapped_column(Integer, ForeignKey("models.id"), nullable=False)
    brand_id: Mapped[int] = mapped_column(Integer, ForeignKey("brands.id"), nullable=False)
    location_id: Mapped[int] = mapped_column(Integer, ForeignKey("locations.id"), nullable=False)
    emission_standard_id: Mapped[int] = mapped_column(Integer, ForeignKey("emission_standards.id"), nullable=False)
    drivetrain_id: Mapped[int] = mapped_column(Integer, ForeignKey("drivetrains.id"), nullable=False)
    transmission_id: Mapped[int] = mapped_column(Integer, ForeignKey("transmissions.id"), nullable=False)
    vehicle_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("vehicle_types.id"), nullable=False)
    body_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("body_types.id"), nullable=False)

    # relationship attributes
    images: Mapped[list["Image"]] = relationship("Image", back_populates="post", cascade="all, delete-orphan")
    equipments: Mapped[list["Equipment"]] = relationship(secondary="post_equipments", back_populates="posts")

    user: Mapped["User"] = relationship(back_populates="posts")
    fuel: Mapped["Fuel"] = relationship(back_populates="posts")
    model: Mapped["Model"] = relationship(back_populates="posts")
    brand: Mapped["Brand"] = relationship(back_populates="posts")
    location: Mapped["Location"] = relationship(back_populates="posts")
    emission_standard: Mapped["EmissionStandard"] = relationship(back_populates="posts")
    drivetrain: Mapped["Drivetrain"] = relationship(back_populates="posts")
    transmission: Mapped["Transmission"] = relationship(back_populates="posts")
    vehicle_type: Mapped["VehicleType"] = relationship(back_populates="posts")
    body_type: Mapped["BodyType"] = relationship(back_populates="posts")

