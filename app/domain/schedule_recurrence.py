from app.core.database import Base

from sqlalchemy import Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import mapped_column, relationship

class ScheduleRecurrence(Base):
    __tablename__ = "schedule_recurrence"

    id = mapped_column(Integer, primary_key=True)
    schedule_id = mapped_column(
        ForeignKey("schedules.id"),
        unique=True
    )

    freq = mapped_column(String)
    interval = mapped_column(Integer, default=1)
    by_weekday = mapped_column(String, nullable=True)
    until = mapped_column(DateTime, nullable=True)

    schedule = relationship("Schedule", back_populates="recurrence")