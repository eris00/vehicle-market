from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from app.models.posts import Post
from app.schemas.equipments import EquipmentBase
from app.schemas.images import ImageRequest, ImageResponse
from app.schemas.location import LocationBase
from app.schemas.user import UserResponse

class PostBase(BaseModel):
    title: str
    description: Optional[str]
    price: float
    year: int
    mileage: int
    engine_displacement: float
    kilowatts: int
    horsepowers: int
    color: str
    doors_number: Optional[str]
    payload_capacity: Optional[str]
    axle_count: Optional[str]

class PostRequest(PostBase):
    user_id: int
    fuel_id: int
    model_id: int
    brand_id: int
    location_id: int
    emission_standard_id: int
    drivetrain_id: int
    transmission_id: int
    vehicle_type_id: int
    body_type_id: int
    equipment_ids: List[int]
    images: List[ImageRequest]

class PostResponse(PostBase):
    id: int
    user: UserResponse
    images: List[ImageResponse]
    fuel: str
    brand: str
    model: str
    location: LocationBase
    emission_standard: str
    drivetrain: str
    transmission: str
    vehicle_type: str
    body_type: str
    equipment: List[EquipmentBase]


    @classmethod
    def from_orm(cls, post: Post):
        return cls(
            id=post.id,
            title=post.title,
            description=post.description,
            price=post.price,
            year=post.year,
            mileage=post.mileage,
            engine_displacement=post.engine_displacement,
            images=[ImageResponse.model_validate(img) for img in post.images],
            kilowatts=post.kilowatts,
            horsepowers=post.horsepowers,
            color=post.color,
            doors_number=post.doors_number,
             payload_capacity=post.payload_capacity,
            axle_count=post.axle_count,
            user=UserResponse.model_validate(post.user),
            fuel=post.fuel.name if post.fuel else None,
            brand=post.brand.name if post.brand else None,
            model=post.model.name if post.model else None,
            location=LocationBase.model_validate(post.location),
            emission_standard=post.emission_standard.name if post.emission_standard else None,
            drivetrain=post.drivetrain.name if post.drivetrain else None,
            transmission=post.transmission.name if post.transmission else None,
            vehicle_type=post.vehicle_type.name if post.vehicle_type else None,
            body_type=post.body_type.name if post.body_type else None,
            equipment=[EquipmentBase.model_validate(equip) for equip in post.equipments],
        )
    
    model_config = ConfigDict(from_attributes=True)
