from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_setting():
    setting = {
        "version": "1.0.0",
    }
    return setting
