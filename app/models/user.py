from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped,  mapped_column, relationship

from datetime import datetime

from .base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))

    created_at: Mapped[datetime] = mapped_column(default=datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(datetime.timezone.utc),
        onupdate=datetime.now(datetime.timezone.utc)
    )

    life_areas = relationship("LifeArea", back_populates="user")
    schedules = relationship("Schedule", back_populates="user")
