from typing import List
from pydantic import BaseModel

from app.schemas.models import ModelBrand

class BrandBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class BrandResponse(BrandBase):
    models: List[ModelBrand]
