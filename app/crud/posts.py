import os
from typing import Any, Dict
from uuid import uuid4
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from sqlalchemy.orm import joinedload
from app.models.body_types import BodyType
from app.models.brands import Brand
from app.models.drivetrains import Drivetrain
from app.models.emission_standards import EmissionStandard
from app.models.fuels import Fuel
from app.models.images import Image
from app.models.location import Location
from app.models.models import Model
from app.models.posts import Post
from app.models.user import User
from app.models.vehicle_types import VehicleType
from app.schemas.images import ImageRequest
from app.schemas.posts import PostRequest, PostResponse
from app.models.transmissions import Transmission
from app.core.config import settings
from app.models.equipments import post_equipments
from pathlib import Path as FilePath


ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

def get_post_by_id(db: Session, post_id: int) -> Post:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user),
            joinedload(Post.fuel).load_only(Fuel.name),
            joinedload(Post.model).load_only(Model.name),
            joinedload(Post.brand).load_only(Brand.name),
            joinedload(Post.emission_standard).load_only(EmissionStandard.name),
            joinedload(Post.drivetrain).load_only(Drivetrain.name),
            joinedload(Post.transmission).load_only(Transmission.name),
            joinedload(Post.vehicle_type).load_only(VehicleType.name),
            joinedload(Post.body_type).load_only(BodyType.name),
            joinedload(Post.location),
            joinedload(Post.images),
            joinedload(Post.equipments),
        )
        .where(Post.id == post_id)
    )
    result = db.execute(stmt).unique().scalar_one_or_none()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Post with ID {post_id} does not exist."
        )
    return result

def get_posts(db: Session, user_id: int = None):
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user),
            joinedload(Post.fuel).load_only(Fuel.name),
            joinedload(Post.model).load_only(Model.name),
            joinedload(Post.brand).load_only(Brand.name),
            joinedload(Post.emission_standard).load_only(EmissionStandard.name),
            joinedload(Post.drivetrain).load_only(Drivetrain.name),
            joinedload(Post.transmission).load_only(Transmission.name),
            joinedload(Post.vehicle_type).load_only(VehicleType.name),
            joinedload(Post.body_type).load_only(BodyType.name),
            joinedload(Post.location),
            joinedload(Post.images),
            joinedload(Post.equipments)
        )
    )

    if user_id is not None:
        stmt = stmt.where(Post.user_id == user_id)

    result = db.execute(stmt)
    posts = result.unique().scalars().all()
    return posts

def create_post(db: Session, post_data: PostRequest):
        # add posts attributes
        new_post = Post(**post_data.model_dump(exclude={"equipment_ids", "images"}))
        db.add(new_post)
        db.flush()
        # add equipment relations
        if post_data.equipment_ids:
            stmt = insert(post_equipments).values([
            {"post_id": new_post.id, "equipment_id": equipment_id} for equipment_id in post_data.equipment_ids
        ])
        db.execute(stmt)
        # add images to post
        save_images(db, post_id=new_post.id, images=post_data.images)

        db.commit()
        return new_post     

      
def save_images(db: Session, post_id: int, images: list[ImageRequest]):
    # Validate file extensions
    invalid_files = [image.image_url.filename for image in images if image.image_url.filename.split('.')[-1].lower() not in ALLOWED_EXTENSIONS]
    if invalid_files:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid file types: {', '.join(invalid_files)}. Allowed types are: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    images_to_save = []

    for image_request in images:
        file = image_request.image_url

        # Generate filename and path
        filename = f"{uuid4()}.{file.filename.split('.')[-1].lower()}"
        filepath = os.path.join(settings.POSTS_IMAGE_DIR, filename)

        # Save file to disk
        with open(filepath, "wb") as f:
            f.write(file.file.read())

        # Create Image instance
        images_to_save.append(Image(
            post_id=post_id,
            image_url=f"/media/posts/{filename}",
            is_primary=image_request.is_primary
        ))

    # Batch save to the database
    db.bulk_save_objects(images_to_save)
    db.commit()

def update_post(db: Session, post_id: int, updates: Dict[str, Any]):

    post = db.query(Post).filter(Post.id == post_id).one_or_none()
    if not post:
        raise ValueError(f"Post with ID {post_id} does not exist.")
    
    for key, value in updates.items():
        if hasattr(post, key):
            setattr(post, key, value)
    
    db.commit()
    db.refresh(post)
    return post


def delete_post_by_id(db: Session, post_id: int):
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail=f"Post with ID {post_id} does not exist."
        )

    # Delete files from the directory
    for image in post.images:
        image_path = FilePath(image.image_url.lstrip("/"))
        if image_path.exists():
            image_path.unlink()

    db.delete(post)
    db.commit()
    return {"message": f"Post with ID {post_id} has been deleted successfully."}