from typing import List, Optional
from pydantic import BaseModel

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


"""

Example:
{
    "title": "Audi A4",
    "price": 20000.0,
    "year": 2018,
    "mileage": 50000,
    "engine_displacement": 2.0,
    "kilowatts": 140,
    "horsepowers": 190,
    "color": "Black",
    "user_id": 1,
    "fuel_id": 2,
    "model_id": 3,
    "brand_id": 1,
    "location_id": 4,
    "emission_standard_id": 5,
    "drivetrain_id": 6,
    "transmission_id": 7,
    "vehicle_type_id": 8,
    "body_type_id": 9,
    "equipment_ids": [1, 2, 3]
}

"""