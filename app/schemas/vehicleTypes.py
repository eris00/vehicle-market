from typing import List
from pydantic import BaseModel

from app.schemas.bodyTypes import BodyVehicle

class VehicleTypeBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class VehicleTypeResponse(VehicleTypeBase):
    body_types: List[BodyVehicle]