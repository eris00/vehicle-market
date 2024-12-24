from pydantic import BaseModel, ConfigDict

class EquipmentBase(BaseModel):
    id: int
    name: str
    category_id: int

    model_config = ConfigDict(from_attributes=True)  
