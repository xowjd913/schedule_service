from fastapi import APIRouter, HTTPException, status

from app.schemas.schedule import ScheduleCreate, ScheduleResponse
from app.services.schedule import create_schedule, get_schedule

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"]
)

@router.post("/", response_model=ScheduleResponse)
def api_create_schedule(schedule: ScheduleCreate):
    return create_schedule(schedule)

@router.get("/{schedule_id}", response_model=ScheduleResponse)
def api_get_schedule(schedule_id: int):
    schedule = get_schedule(schedule_id)
    if not schedule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Schedule not found"
        )
    
    return schedule