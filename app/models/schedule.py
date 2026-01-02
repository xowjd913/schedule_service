from pydantic import BaseModel
from datetime import date

class Schedule(BaseModel):
    id: int

    title: str
    description: str | None
    
    date: date