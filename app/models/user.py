from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class User(Base):
    __tablename__= "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user")

        
