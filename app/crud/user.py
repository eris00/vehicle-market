from fastapi import Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models.user import User
from schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db:Session, email:str):
    return db.query(User).filter(User.email == email).first()

def create_user(db:Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, first_name=user.first_name, last_name=user.last_name, phone_number=user.phone_number, is_active=user.is_active, has_viber=user.has_viber, has_whatsapp=user.has_whatsapp)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password: str, hash_password: str) -> bool:
    return pwd_context.verify(plain_password, hash_password)
