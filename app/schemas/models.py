from pydantic import BaseModel

class ModelBase(BaseModel):
    id: int
    name: str
    brand_id: int

    class Config:
        orm_mode = True
