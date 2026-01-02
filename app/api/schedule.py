from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.schemas.schedule import ScheduleCreate, ScheduleResponse, ScheduleStatusUpdate, ScheduleStatus

from app.core.database import get_db
from app.schemas.schedule import (
    ScheduleCreate,
    ScheduleResponse,
    ScheduleStatusUpdate,
)

from app.domain.schedule import ScheduleStatus
from app.repositories.schedule_repo import ScheduleRepository
from app.services.schedule_service import ScheduleService

repo = ScheduleRepository()
service = ScheduleService(repo)


router = APIRouter(
    prefix="/schedules",
    tags=["schedules"]
)

@router.post("/", response_model=ScheduleResponse)
def api_create_schedule(
    body: ScheduleCreate,
    db: Session = Depends(get_db)
):
    try:
        return service.create_schedule(
            db=db,
            title=body.title,
            scheduled_at=body.scheduled_at
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{schedule_id}", response_model=ScheduleResponse)
def api_get_schedule(
    schedule_id: int,
    db: Session = Depends(get_db),
):
    schedule = repo.get_by_id(db, schedule_id)
    if not schedule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Schedule not found"
        )
    return schedule
    

@router.patch("/{schedule_id}/status")
def api_patch_schedule_status(
    schedule_id: int,
    body: ScheduleStatusUpdate,
    db: Session = Depends(get_db)
):
    try:
        return service.change_status(
            db,
            schedule_id,
            body,
        )
    except ValueError as e:
        message = str(e)

        if message == "일정을 찾을 수 없습니다":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message
            )
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )
