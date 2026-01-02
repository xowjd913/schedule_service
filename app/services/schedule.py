from app.models.schedule import Schedule, ScheduleStatus
from app.schemas.schedule import ScheduleCreate

from app.db.database import add_schedule, get_schedule_by_id

from fastapi import HTTPException

def create_schedule(schedule_create: ScheduleCreate) -> Schedule:
    new_schedule = Schedule(
        id=0,
        **schedule_create.model_dump(),
    )

    return add_schedule(new_schedule)

def get_schedule(schedule_id: int) -> Schedule | None:
    return get_schedule_by_id(schedule_id)

def update_schedule_status(schedule_id: int, status: ScheduleStatus) -> Schedule | None:
    schedule = get_schedule_by_id(schedule_id)

    if schedule is None:
        raise ValueError("Schedule not found")

    if schedule.status == ScheduleStatus.DONE:
        raise ValueError("Same status")
    
    if schedule.status == ScheduleStatus.CANCELLED and status == ScheduleStatus.DONE:
        raise ValueError("CANCELLED to DONE not allowed")
    
    schedule.status = status

    return schedule