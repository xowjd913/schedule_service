from pydantic import BaseModel
from datetime import date

from enum import Enum

class ScheduleStatus(str, Enum):
    PENDING = "PENDING"
    DONE = "DONE"
    CANCELLED = "CANCELLED"

class Schedule(BaseModel):
    id: int

    title: str
    description: str | None
    
    date: date

    status: ScheduleStatus = ScheduleStatus.PENDING

class ScheduleStatusUpdate(BaseModel):
    status: ScheduleStatus