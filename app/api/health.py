from fastapi import APIRouter

router = APIRouter(
    prefix="/cores",
    tags=["/cores"]
)

@router.get("/")
def health_check():
    return {"status": "ok"}