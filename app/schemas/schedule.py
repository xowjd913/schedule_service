from pydantic import BaseModel, ConfigDict
from datetime import datetime

from app.models.schedule import ScheduleStatus
from app.schemas.schedule_recurrence import RecurrenceResponse, RecurrenceCreate

class ScheduleCreate(BaseModel):
    title: str
    description: str | None = None

    start_at: datetime
    end_at: datetime

    is_all_day: bool = False

    recurrence: RecurrenceCreate | None = None

class ScheduleResponse(BaseModel):
    id: int
    title: str
    description: str | None

    start_at: datetime
    end_at: datetime
    
    is_all_day: bool
    
    recurrence: RecurrenceResponse | None

    model_config = ConfigDict(from_attributes=True)

class ScheduleStatusUpdate(BaseModel):
    status: ScheduleStatus = ScheduleStatus.PENDING