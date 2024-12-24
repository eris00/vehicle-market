from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class Images(BaseModel):
    image_url: str
    is_primary: bool
    
    model_config = ConfigDict(from_attributes=True)
