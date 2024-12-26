
from typing import List, Optional
from app.crud.posts import create_post, delete_post_by_id, get_post_by_id, get_posts, update_post
from app.models.posts import Post
from app.schemas.images import ImageRequest
from app.schemas.posts import PostCreateRequest, PostRequest, PostResponse, PostUpdateRequest
from app.utils.auth import oauth2_scheme
from app.core.database import db
from fastapi import APIRouter, Depends, File, Form, HTTPException, Path, UploadFile

router = APIRouter(prefix="/posts", tags=["posts"], dependencies=[Depends(oauth2_scheme)])


@router.get("/get_post/{post_id}", response_model=PostResponse)
def get_post(db: db, post_id: int):
    try:
        post = get_post_by_id(db, post_id)
        return PostResponse.from_orm(post)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/get_all_posts", response_model=list[PostResponse])
def get_all_posts(db: db):
    posts = get_posts(db)
    return [PostResponse.from_orm(post) for post in posts]


@router.post("/create_post", response_model=PostResponse, status_code=201)
def create_new_post(
    db: db,
    post_data: PostCreateRequest = Depends(),
    images: List[UploadFile] = File(...)
):
    # Parsing equipment_ids in list
    equipment_ids_list = [int(e.strip()) for e in post_data.equipment_ids.split(",")]

    # Map datas on PostRequest
    post_request = PostRequest(
        **post_data.model_dump(exclude={"equipment_ids"}),
        equipment_ids=equipment_ids_list,
        images=[ImageRequest(image_url=image, is_primary=False) for image in images]
    )

    created_post = create_post(db, post_request)
    return PostResponse.from_orm(created_post)

@router.put("/update_post/{post_id}", response_model=PostResponse)
def update_post_route(
    post_id: int,
    updates: PostUpdateRequest,
    db: db
):
    try:
        updated_post = update_post(db, post_id, updates.dict(exclude_unset=True))
        return PostResponse.from_orm(updated_post)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/delete")
def delete_post_and_images(db: db, post_id: int):
    return delete_post_by_id(db, post_id)
    
