from pydantic import BaseModel, ConfigDict
from datetime import datetime

class RecurrenceCreate(BaseModel):
    freq: str
    interval: int = 1
    by_weekday: str | None = None
    until: datetime | None = None

class RecurrenceResponse(BaseModel):
    freq: str
    interval: int
    by_weekday: str | None
    until: datetime | None
    model_config = ConfigDict(from_attributes=True)