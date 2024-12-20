from pydantic import BaseModel
from typing import List, Optional

class TransmissionBase(BaseModel):
    id: int
    name: str
    number_of_gears: Optional[str] = None

    class Config:
        from_attributes = True