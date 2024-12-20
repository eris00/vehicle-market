from pydantic import BaseModel

class DrivetrainBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
