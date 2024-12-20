from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class EquipmentCategory(Base):
    __tablename__="equipment_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    equipments: Mapped[list["Equipment"]] = relationship("Equipment", back_populates="category")
    
