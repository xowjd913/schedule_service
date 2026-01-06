from datetime import datetime, timezone
from typing import List
from sqlalchemy.orm import Session

from app.domain.schedule import Schedule, ScheduleStatus
from app.domain.schedule_recurrence import ScheduleRecurrence
from app.repositories.schedule_repo import ScheduleRepository
from app.schemas.schedule import ScheduleCreate

class ScheduleService:

    def __init__(self, repo: ScheduleRepository):
        self.repo = repo

    def create_schedule(
            self,
            db: Session,
            user_id: int,
            data: ScheduleCreate
    ) -> Schedule:
        
        schedule = Schedule(
            user_id=user_id,
            title=data.title,
            description=data.description,
            start_at=data.start_at,
            end_at=data.end_at,
            is_all_day=data.is_all_day
        )

        if data.recurrence:
            schedule.recurrence = ScheduleRecurrence(
                freq=data.recurrence.freq,
                interval=data.recurrence.interval,
                by_weekday=data.recurrence.by_weekday,
                until=data.recurrence.until
            )

        return self.repo.save(db, schedule)


    def get_schedules(self, db: Session) -> List[Schedule]:
        return self.repo.get_all(db)
    
    def change_status(
            self,
            db: Session,
            schedule_id: int,
            new_status: ScheduleStatus,
    ) -> Schedule:
        
        schedule = self.repo.get_by_id(db, schedule_id)
        if not schedule:
            raise ValueError("일정을 찾을 수 없습니다")
        if schedule.status == ScheduleStatus.DONE:
            raise ValueError("이미 완료된 일정입니다.")
        
        schedule.status = new_status
        return self.repo.save(db, schedule)
        