from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate

from app.db.database import add_schedule, get_schedule_by_id

def create_schedule(schedule_create: ScheduleCreate) -> Schedule:
    new_schedule = Schedule(
        id=0,
        **schedule_create.model_dump(),
    )

    return add_schedule(new_schedule)

def get_schedule(schedule_id: int) -> Schedule | None:
    return get_schedule_by_id(schedule_id)