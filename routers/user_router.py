from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("",
            summary="Return data of user",
            description="Return data of user")
async def service(user: str):
    return {"teste": user}
