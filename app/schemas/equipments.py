from pydantic import BaseModel

class EquipmentBase(BaseModel):
    id: int
    name: str
    category_id: int

    class Config:
        orm_mode = True
