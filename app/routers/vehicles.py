from typing import List
from app.crud.tranmissions import get_all_transmissions
from app.models.body_types import BodyType
from app.models.brands import Brand
from app.models.drivetrains import Drivetrain
from app.models.emission_standards import EmissionStandard
from app.models.equipment_categories import EquipmentCategory
from app.models.equipments import Equipment
from app.models.fuels import Fuel
from app.models.location import Location
from app.models.models import Model
from app.models.vehicle_types import VehicleType
from app.schemas.brands import BrandBase
from app.schemas.drivetrains import DrivetrainBase
from app.schemas.emissionStandards import EmissionStandardBase
from app.schemas.equipmentCategory import EquipmentCategoryBase
from app.schemas.equipments import EquipmentBase
from app.schemas.fuels import FuelBase
from app.schemas.location import LocationBase
from app.schemas.models import ModelBase
from app.schemas.transmissions import TransmissionBase
from app.schemas.vehicleTypes import VehicleTypeBase
from app.schemas.bodyTypes import BodyTypeBase
from app.utils.auth import oauth2_scheme
from app.core.database import db
from fastapi import APIRouter, Depends, HTTPException
from app.models.transmissions import Transmission

router = APIRouter(prefix="/vehicles", tags=["vehicles"], dependencies=[Depends(oauth2_scheme)])

@router.get("/vehicle-types", response_model=List[VehicleTypeBase])
def get_transmissions_route(db: db):
    return db.query(VehicleType).all()

@router.get("/body-types", response_model=List[BodyTypeBase])
def get_transmissions_route(db: db):
    return db.query(BodyType).all()

@router.get("/brands", response_model=List[BrandBase])
def get_transmissions_route(db: db):
    return db.query(Brand).all()

@router.get("/models", response_model=List[ModelBase])
def get_transmissions_route(db: db):
    return db.query(Model).all()

@router.get("/transmissions", response_model=List[TransmissionBase])
def get_transmissions_route(db: db):
    return db.query(Transmission).all()

@router.get("/fuels", response_model=List[FuelBase])
def get_transmissions_route(db: db):
    return db.query(Fuel).all()

@router.get("/drivetrains", response_model=List[DrivetrainBase])
def get_transmissions_route(db: db):
    return db.query(Drivetrain).all()

@router.get("/emission-standards", response_model=List[EmissionStandardBase])
def get_transmissions_route(db: db):
    return db.query(EmissionStandard).all()

@router.get("/equipment-categories", response_model=List[EquipmentCategoryBase])
def get_transmissions_route(db: db):
    return db.query(EquipmentCategory).all()

@router.get("/equipments", response_model=List[EquipmentBase])
def get_transmissions_route(db: db):
    return db.query(Equipment).all()

@router.get("/locations", response_model=List[LocationBase])
def get_transmissions_route(db: db):
    return db.query(Location).all()