from fastapi import FastAPI
from app.api.schedule import router as api_schedule_router
from app.api.health import router as api_health_check_router

from app.core.database import engine, Base

app = FastAPI(
    title="Schedule Service"
)

app.include_router(api_schedule_router)
app.include_router(api_health_check_router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
