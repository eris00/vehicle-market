from pydantic import BaseModel

class LocationBase(BaseModel):
    id: int
    city: str
    country: str
    region: str | None

    class Config:
        orm_mode = True
