
from sqlalchemy import (
    String, Date, Boolean, Enum, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

from .base import Base
from .schedule_status import ScheduleStatus

class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    life_area_id: Mapped[int] = mapped_column(ForeignKey("life_areas.id"))

    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None]

    start_date: Mapped[datetime]
    end_date: Mapped[datetime | None]

    is_all_day: Mapped[bool] = mapped_column(Boolean, default=False)

    status: Mapped[ScheduleStatus] = mapped_column(
        Enum(ScheduleStatus),
        default=ScheduleStatus.PLANNED
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(datetime.timezone.utc),
        onupdate=datetime.now(datetime.timezone.utc)
    )

    user = relationship("User", back_populates="schedules")
    life_area = relationship("LifeArea", back_populates="schedules")
    histories = relationship(
        "ScheduleHistory",
        back_populates="schedule",
        cascade="all, delete_orphan"
    )

