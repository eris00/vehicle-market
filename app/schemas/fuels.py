from pydantic import BaseModel

class FuelBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
