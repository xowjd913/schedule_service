from typing import List

from app.models.schedule import Schedule

schedules: List[Schedule] = []
next_id = 1

def add_schedule(schedule: Schedule) -> Schedule:

    global next_id
    schedule.id = next_id
    schedules.append(schedule)

    next_id += 1

    return schedule

def get_schedule_by_id(schedule_id: int) -> Schedule | None:
    for schedule in schedules:
        if schedule.id == schedule_id:
            return schedule
        
        return None