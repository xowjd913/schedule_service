from sqlalchemy.orm import Session
from typing import List, Optional

from app.domain.schedule import Schedule

class ScheduleRepository:
    def create(self, db: Session, schedule: Schedule) -> Schedule:
        db.add(schedule)
        db.commit()
        db.refresh(schedule)

        return schedule
    
    def get_by_id(self, db: Session, schedule_id: int) -> Optional[Schedule]:
        return (
            db.query(Schedule)
            .filter(Schedule.id == schedule_id)
            .first()
        )
    
    def get_all(self, db: Session) -> List[Schedule]:
        return db.query(Schedule).all()
    
    def save(self, db: Session, schedule: Schedule) -> Schedule:
        db.add(schedule)
        db.commit()
        db.refresh(schedule)

        return schedule