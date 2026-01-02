from fastapi import FastAPI
from app.api.schedule import router as api_schedule_router
from app.api.health import router as api_health_check_router

app = FastAPI(
    title="Schedule Service"
)

app.include_router(api_schedule_router)
app.include_router(api_health_check_router)

