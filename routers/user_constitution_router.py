from fastapi import APIRouter, HTTPException
import core.schemes as schemes
import internal

router = APIRouter()

@router.get("/user_constitution/{id_user}",
            summary="Return data of the user physical constitution by id_user",
            description="Return data of the user physical constitution by id_user",
            response_description="Returns constitution data from user",
            response_model=schemes.user_constitution_schemes.User_Constitution_GetResponse,
            operation_id="GetUserConstitutionByIdUser"
            )
async def service(id_user: str):
    validate = internal.validate_uuid.is_uuid_valid(id_user)
    if validate is True:
        return {"msg": "success", "data":{}}
    else:
        return {"msg": "error", "data": {}}