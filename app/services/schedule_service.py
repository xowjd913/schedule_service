from datetime import datetime, timezone
from typing import List
from sqlalchemy.orm import Session

from app.domain.schedule import Schedule, ScheduleStatus
from app.repositories.schedule_repo import ScheduleRepository

class ScheduleService:

    def __init__(self, repo: ScheduleRepository):
        self.repo = repo

    def create_schedule(
            self,
            db: Session,
            title: str,
            scheduled_at: datetime
    ) -> Schedule:
        
        now = datetime.now(timezone.utc)

        if scheduled_at < now:
            raise ValueError("과거 일정은 생산 불가능.")
        
        schedule = Schedule(
            title=title,
            scheduled_at=scheduled_at,
            status=ScheduleStatus.PENDING
        )

        return self.repo.create(db, schedule)
    
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
        