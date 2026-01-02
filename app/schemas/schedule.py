from pydantic import BaseModel, ConfigDict
from datetime import datetime

from app.models.schedule import ScheduleStatus

class ScheduleCreate(BaseModel):
    title: str
    description: str | None = None

    scheduled_at: datetime

    status: ScheduleStatus = ScheduleStatus.PENDING

class ScheduleResponse(BaseModel):
    id: int

    title: str
    description: str | None = None

    scheduled_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ScheduleStatusUpdate(BaseModel):
    status: ScheduleStatus = ScheduleStatus.PENDING