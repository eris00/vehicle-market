
from app.crud.posts import get_posts
from app.schemas.posts import PostResponse
from app.utils.auth import oauth2_scheme
from app.core.database import db
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/posts", tags=["posts"], dependencies=[Depends(oauth2_scheme)])

@router.get("/get_posts", response_model=list[PostResponse])
def get_all_posts(db: db):
    posts = get_posts(db)
    return [PostResponse.from_orm(post) for post in posts]
    
    
