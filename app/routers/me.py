from fastapi import APIRouter, Depends, HTTPException
from app.crud.posts import get_posts
from app.crud.user import update_user
from app.schemas.posts import PostResponse
from app.schemas.user import UserBase, UserResponse, UserUpdate
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

@router.put("/update_user/{user_id}", response_model=UserResponse)
def update_user_route(
    user_id: int,
    updates: UserUpdate,
    db: db
):
    try:
        updated_user = update_user(db, user_id, updates.model_dump(exclude_unset=True))
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))