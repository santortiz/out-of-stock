from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
async def test():
    return {"message": "Hello, World!"}