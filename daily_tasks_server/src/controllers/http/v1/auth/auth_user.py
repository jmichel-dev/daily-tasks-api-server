from fastapi import APIRouter, status

router = APIRouter()


@router.post('', status_code=status.HTTP_201_CREATED)
async def signup() -> dict:
    return {"msg": "Hello, World"}
