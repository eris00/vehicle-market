from typing import List, Optional
from fastapi import UploadFile
from pydantic import BaseModel, ConfigDict

class ImageBase(BaseModel):
    is_primary: bool
    model_config = ConfigDict(from_attributes=True)

class ImageResponse(ImageBase):
    image_url: str

class ImageRequest(ImageBase):
    image_url: UploadFile
