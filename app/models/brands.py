from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class Brand(Base):
    __tablename__="brands"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    models: Mapped[list["Model"]] = relationship("Model", back_populates="brand")
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="brand")
    
