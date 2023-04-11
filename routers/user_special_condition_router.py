from fastapi import APIRouter, HTTPException, Response, status
import core.schemes as schemes
import internal


router = APIRouter()

@router.get("/by-id/{id_user}",
            summary="Return data of user special condition by id_user",
            description="Return data of user special condition by id_user",
            response_description="Returns special condition data from user",
            response_model=schemes.user_special_conditions_schemes.UserSpecialConditionGetResponse,
            operation_id="GetDataUserByIdUser"
            )
async def service(response:Response, id_user: str):
    validate = internal.validate_uuid.is_uuid_valid(id_user)
    if validate is True:
        return {"msg": "success", "data":{}}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg": "error", "data": "This ID is invalid"}