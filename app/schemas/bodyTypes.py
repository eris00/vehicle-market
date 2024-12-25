from pydantic import BaseModel

class BodyTypeBase(BaseModel):
    id: int
    name: str
    vehicle_type_id: int

    class Config:
        orm_mode = True

class BodyVehicle(BaseModel):
    id: int
    name: str