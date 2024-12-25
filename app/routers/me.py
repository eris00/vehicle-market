from fastapi import APIRouter, Depends
from app.crud.posts import get_posts
from app.schemas.posts import PostResponse
from app.schemas.user import UserBase, UserResponse
from app.utils.auth import get_current_user, oauth2_scheme
from app.core.database import db


router = APIRouter(prefix="/me", tags=["me"], dependencies=[Depends(oauth2_scheme)])


@router.get("", response_model=UserResponse)
def read_current_user(current_user: UserBase = Depends(get_current_user)):
    return current_user


@router.get("/get_user_posts/{user_id}", response_model=list[PostResponse])
def get_user_posts(user_id: int, db: db):
    posts = get_posts(db, user_id=user_id)
    return [PostResponse.from_orm(post) for post in posts]