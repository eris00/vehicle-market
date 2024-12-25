from fastapi import Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db:Session, email:str):
    return db.query(User).filter(User.email == email).first()

def create_user(db:Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, first_name=user.first_name, last_name=user.last_name, phone_number=user.phone_number, is_active=user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password: str, hash_password: str) -> bool:
    return pwd_context.verify(plain_password, hash_password)

def update_user(db: Session, user_id: int, updates: dict):
    user = db.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        raise ValueError(f"User with ID {user_id} does not exist.")
    
    for key, value in updates.items():
        if key == "password" and value:
            setattr(user, key, pwd_context.hash(value))
        elif value is not None:
            setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user