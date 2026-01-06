from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String, unique=True, index=True)
    name = mapped_column(String)
    created_at = mapped_column(
        DateTime,
        default=datetime.now(datetime.timezone.utc)
    )

    schedules = relationship("Schedule", back_populates="user")
