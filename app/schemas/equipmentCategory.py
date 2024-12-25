from typing import List
from pydantic import BaseModel

class EquipmentCategoryBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class EquipmentCategory(BaseModel):
    id: int
    name: str

class EquipmentCategoryeResponse(EquipmentCategoryBase):
    equipments: List[EquipmentCategory]