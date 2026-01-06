from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import String, DateTime, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Enum as SqlEnum

from app.core.database import Base
from app.models.schedule import ScheduleStatus

class Schedule(Base):
    __tablename__ = "schedules"

    id = mapped_column(Integer, primary_key=True)

    user_id = mapped_column(ForeignKey("user_id"), index=True)
    
    title = mapped_column(String)
    description = mapped_column(String, nullable=True)

    start_at = mapped_column(DateTime)
    end_at = mapped_column(DateTime)

    is_all_day = mapped_column(Boolean, default=False)

    user = relationship("User", back_populates="schedules")
    recurrence = relationship(
        "ScheduleRecurrence",
        back_populates="schedule",
        uselist=False,
        cascade="all, delete"
    )

