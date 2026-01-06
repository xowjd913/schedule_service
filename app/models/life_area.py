from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

from .base import Base

class LifeArea(Base):
    __tablename__ = "life_areas"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    name: Mapped[str] = mapped_column(String(50))
    color: Mapped[str] = mapped_column(String(20))

    is_default: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.now(datetime.timezone.now))

    user = relationship("User", back_populates="life_areas")
    schedules = relationship("Schedule", back_populates="life_areas")