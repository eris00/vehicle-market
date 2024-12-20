from pydantic import BaseModel

class EmissionStandardBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
