from fastapi import APIRouter, HTTPException
import core.schemes as schemes
import internal


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


@router.get("/by-id/{id_user}",
            summary="Return data of user by id_user",
            description="Return data of user by id_user",
            response_description="Returns basic data from user",
            response_model=schemes.user_schemes.UserGetResponse,
            operation_id="GetDataUserByIdUser"
            )
async def service(id_user: str):
    validate = internal.validate_uuid.is_uuid_valid(id_user)
    if validate is True:
        return {"msg": "success", "data":{}}
    else:
        return {"msg": "error", "data": {}}


@router.put("by-id/{id_user}",
            summary="Updates user data by id_user",
            description="Updates user data by id_user",
            response_description="Updates user",
            response_model=schemes.user_schemes.UserUpdateResponse,
            operation_id="UpdateUserDataByIdUser"
            )
async def update_user(user: schemes.user_schemes.UserPut):
    return {"msg": "success", "data": {}}
