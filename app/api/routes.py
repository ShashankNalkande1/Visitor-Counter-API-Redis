from fastapi import APIRouter, HTTPException
from ..services.like_service import LikeService

router = APIRouter()

@router.get("/likes")
async def get_likes():
    """Return current like count."""
    try:
        count = LikeService.get_likes()
        return {"likes": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis error: {str(e)}")

@router.post("/like")
async def like_photo():
    """Increment like count atomically and return new count."""
    try:
        new_count = LikeService.increment_likes()
        return {"likes": new_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis error: {str(e)}")