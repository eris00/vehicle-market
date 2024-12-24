from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from app.models.body_types import BodyType
from app.models.brands import Brand
from app.models.drivetrains import Drivetrain
from app.models.emission_standards import EmissionStandard
from app.models.fuels import Fuel
from app.models.location import Location
from app.models.models import Model
from app.models.posts import Post
from app.models.user import User
from app.models.vehicle_types import VehicleType
from app.schemas.posts import PostResponse
from app.models.transmissions import Transmission

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