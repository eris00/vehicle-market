from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class Transmission(Base):
    __tablename__="transmissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    number_of_gears: Mapped[str] = mapped_column(String, nullable=True)
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="transmission")
    

    