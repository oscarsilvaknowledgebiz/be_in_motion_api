from fastapi import APIRouter, HTTPException
import core.schemes as schemes


router = APIRouter()


@router.get("/{user}",
            summary="Return data of user",
            description="Return data of user",
            response_description="Returns basic data from user",
            response_model=schemes.user_schemes.UserGetResponse,
            operation_id="GetDataUser"
            )
async def service(user: str):
    return {"msg": "success", "data":{}}
