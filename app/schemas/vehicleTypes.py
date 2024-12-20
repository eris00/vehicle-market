from pydantic import BaseModel

class VehicleTypeBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True