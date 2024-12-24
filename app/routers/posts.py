
from typing import List, Optional
from app.crud.posts import create_post, delete_post_by_id, get_post_by_id, get_posts
from app.models.posts import Post
from app.schemas.images import ImageRequest
from app.schemas.posts import PostRequest, PostResponse
from app.utils.auth import oauth2_scheme
from app.core.database import db
from fastapi import APIRouter, Depends, File, Form, HTTPException, Path, UploadFile
from pathlib import Path as FilePath


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
    title: str = Form(...),
    description: str = Form(None),
    price: float = Form(...),
    year: int = Form(...),
    mileage: int = Form(...),
    engine_displacement: float = Form(...),
    kilowatts: int = Form(...),
    horsepowers: int = Form(...),
    color: str = Form(...),
    doors_number: Optional[str] = Form(None),
    user_id: int = Form(...),
    fuel_id: int = Form(...),
    model_id: int = Form(...),
    brand_id: int = Form(...),
    location_id: int = Form(...),
    emission_standard_id: int = Form(...),
    drivetrain_id: int = Form(...),
    transmission_id: int = Form(...),
    vehicle_type_id: int = Form(...),
    body_type_id: int = Form(...),
    equipment_ids: str = Form(...),
    payload_capacity: Optional[str] = Form(None),
    axle_count: Optional[str] = Form(None),
    images: List[UploadFile] = File(...)
):

    equipment_ids_list = [int(e.strip()) for e in equipment_ids.split(",")]

    post_data = PostRequest(
        title=title,
        description=description,
        price=price,
        year=year,
        mileage=mileage,
        engine_displacement=engine_displacement,
        kilowatts=kilowatts,
        horsepowers=horsepowers,
        color=color,
        doors_number=doors_number,
        user_id=user_id,
        fuel_id=fuel_id,
        model_id=model_id,
        brand_id=brand_id,
        location_id=location_id,
        emission_standard_id=emission_standard_id,
        drivetrain_id=drivetrain_id,
        transmission_id=transmission_id,
        vehicle_type_id=vehicle_type_id,
        body_type_id=body_type_id,
        equipment_ids=equipment_ids_list,
        payload_capacity=payload_capacity,
        axle_count=axle_count,
        images=[ImageRequest(image_url=image, is_primary=False) for image in images]
    )

    created_post = create_post(db, post_data)
    return PostResponse.from_orm(created_post)

@router.delete("/delete")
def delete_post_and_images(db: db, post_id: int):
    post = get_post_by_id(db, post_id)
    if not post:
        raise ValueError(f"Post with ID {post_id} does not exist.")

    # Delete files from the directory
    for image in post.images:
        image_path = FilePath("media/posts") / image.image_url
        if image_path.exists():
            image_path.unlink()

    for image in post.images:
        db.delete(image)

    db.delete(post)
    db.commit()
    
