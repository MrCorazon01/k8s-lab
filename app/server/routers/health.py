from fastapi import APIRouter

router = APIRouter()

@router.get("/health/ready")
async def readiness():
    return {"status": "ready"}

@router.get("/health/live")
async def liveness():
    return {"status": "alive"}
