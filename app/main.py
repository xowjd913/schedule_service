from fastapi import FastAPI
from app.api.router import router

app = FastAPI(
    title="Schedule Service"
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}


