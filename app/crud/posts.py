import os
from uuid import uuid4
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
    print("RESULT IS HERE: ", result.fuel.name)
    if not result:
        raise ValueError(f"Post with ID {post_id} does not exist.")
    return result

def get_posts(db: Session):
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

    result = db.execute(stmt)
    posts = result.unique().scalars().all()
    return posts

def create_post(db: Session, post_data: PostRequest):
        
        # add posts attributes
        new_post = Post(
            user_id=post_data.user_id,
            title=post_data.title,
            description=post_data.description,
            price=post_data.price,
            year=post_data.year,
            mileage=post_data.mileage,
            engine_displacement=post_data.engine_displacement,
            kilowatts=post_data.kilowatts,
            horsepowers=post_data.horsepowers,
            color=post_data.color,
            doors_number=post_data.doors_number,
            fuel_id=post_data.fuel_id,
            model_id=post_data.model_id,
            brand_id=post_data.brand_id,
            location_id=post_data.location_id,
            emission_standard_id=post_data.emission_standard_id,
            drivetrain_id=post_data.drivetrain_id,
            transmission_id=post_data.transmission_id,
            vehicle_type_id=post_data.vehicle_type_id,
            body_type_id=post_data.body_type_id,
            payload_capacity=post_data.payload_capacity,
            axle_count=post_data.axle_count,
        )
        db.add(new_post)
        db.flush()

        # add equipment relations
        for equipment_id in post_data.equipment_ids:
                stmt = insert(post_equipments).values(post_id=new_post.id, equipment_id=equipment_id)
                db.execute(stmt)

        # add images to post
        save_images(db, post_id=new_post.id, images=post_data.images)

        db.commit()

        return new_post
        

      

def save_images(db: Session, post_id: int, images: list[ImageRequest]):

    for image_request in images:

        file = image_request.image_url
        is_primary = image_request.is_primary

        # Check file extensions
        file_extension = file.filename.split('.')[-1].lower()
        if file_extension not in ALLOWED_EXTENSIONS:
            raise ValueError(f"Invalid file type: {file.filename}. Allowed types are: {', '.join(ALLOWED_EXTENSIONS)}")

        # Generate a file name
        filename = f"{uuid4()}.{file.filename.split('.')[-1]}"
        filepath = os.path.join(settings.POSTS_IMAGE_DIR, filename)

        # Save file
        with open(filepath, "wb") as f:
            f.write(file.file.read())

        # Write in database
        db_image = Image(
            post_id=post_id,
            image_url=f"/media/posts/{filename}",
            is_primary=is_primary
        )
        db.add(db_image)

    db.commit()

def delete_post_by_id(db: Session, post_id: int):
    post = get_post_by_id(db, post_id)
    if not post:
        raise ValueError(f"Post with ID {post_id} does not exist.")
    db.delete(post)
    db.commit()
    return {"message": f"Post with ID {post_id} has been deleted successfully."}