from pydantic import BaseModel
from datetime import datetime

from enum import Enum

class ScheduleStatus(str, Enum):
    PENDING = "PENDING"
    DONE = "DONE"
    CANCELLED = "CANCELLED"

class Schedule(BaseModel):
    id: int

    title: str
    description: str | None
    
    date: datetime

    status: ScheduleStatus = ScheduleStatus.PENDING

class ScheduleStatusUpdate(BaseModel):
    status: ScheduleStatus