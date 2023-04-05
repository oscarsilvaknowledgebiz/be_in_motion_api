from fastapi import APIRouter, HTTPException
import core.schemes as schemes
import internal


router = APIRouter()

@router.get("/by-id/{id_user}",
            summary="Return data of user special condition by id_user",
            description="Return data of user special condition by id_user",
            response_description="Returns special condition data from user",
            response_model=schemes.user_schemes.UserGetResponse,
            operation_id="GetDataUserByIdUser"
            )
async def service(id_user: str):
    validate = internal.validate_uuid.is_uuid_valid(id_user)
    if validate is True:
        return {"msg": "success", "data":{}}
    else:
        return {"msg": "error", "data": {}}