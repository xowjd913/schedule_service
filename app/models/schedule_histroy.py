from sqlalchemy import DateTime, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from .base import Base
from .schedule_status import ScheduleStatus

class ScheduleHistory(Base):
    __tablename__ = "schedule_history"

    id: Mapped[int] = mapped_column(primary_key=True)

    schedule_id: Mapped[int] = mapped_column(
        ForeignKey("schedules.id")
    )
    
    old_status: Mapped[ScheduleStatus]
    new_status: Mapped[ScheduleStatus]

    old_start_date: Mapped[datetime | None]
    new_start_date: Mapped[datetime | None]

    reason: Mapped[str | None] = mapped_column(String(255))
    changed_at: Mapped[datetime] = mapped_column(
        default=datetime.now(datetime.timezone.utc)
    )

    schedule = relationship("Schedule", back_populates="histories")
    