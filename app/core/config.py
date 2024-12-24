from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 90))

    # media configurations
    ROOT_DIR: str = Path(__file__).resolve().parent.parent.parent
    MEDIA_DIR: str = os.path.join(ROOT_DIR, "media")
    POSTS_IMAGE_DIR: str = os.path.join(MEDIA_DIR, "posts")

    def __init__(self):
        # create them if they don't exist 
        os.makedirs(self.MEDIA_DIR, exist_ok=True)
        os.makedirs(self.POSTS_IMAGE_DIR, exist_ok=True)

settings = Settings()