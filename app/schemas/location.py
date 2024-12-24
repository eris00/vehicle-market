from pydantic import BaseModel, ConfigDict

class LocationBase(BaseModel):
    id: int
    city: str
    country: str
    region: str | None

    model_config = ConfigDict(from_attributes=True)  
