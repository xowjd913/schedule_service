from fastapi import APIRouter, HTTPException, status

from app.schemas.schedule import ScheduleCreate, ScheduleResponse, ScheduleStatusUpdate, ScheduleStatus
from app.services.schedule import create_schedule, get_schedule, update_schedule_status

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

@router.patch("/{schedule_id}/status")
def api_patch_schedule_status(schedule_id: int, body: ScheduleStatusUpdate):
    try:
        return update_schedule_status(schedule_id, body.status)
    except ValueError as e:
        message = str(e)

        if message == "Schedule not found":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message
            )
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )
