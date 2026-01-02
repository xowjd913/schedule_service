from pydantic import BaseModel
from datetime import date

class ScheduleCreate(BaseModel):
    title: str
    description: str | None = None

    date: date

class ScheduleResponse(BaseModel):
    id: int

    title: str
    description: str | None = None

    date: date