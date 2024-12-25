from sqlalchemy import ForeignKey, Integer, String, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

post_equipments = Table(
    "post_equipments",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("equipment_id", ForeignKey("equipments.id", ondelete="CASCADE"), primary_key=True),
)


class Equipment(Base):
    __tablename__="equipments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("equipment_categories.id"), nullable=False)
    category: Mapped["EquipmentCategory"] = relationship("EquipmentCategory", back_populates="equipments")
    posts: Mapped[list["Post"]] = relationship(secondary="post_equipments", back_populates="equipments")

