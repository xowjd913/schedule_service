from pydantic import BaseModel
from datetime import date

from app.models.schedule import ScheduleStatus

class ScheduleCreate(BaseModel):
    title: str
    description: str | None = None

    date: date

    status: ScheduleStatus = ScheduleStatus.PENDING

class ScheduleResponse(BaseModel):
    id: int

    title: str
    description: str | None = None

    date: date

class ScheduleStatusUpdate(BaseModel):
    status: ScheduleStatus = ScheduleStatus.PENDING