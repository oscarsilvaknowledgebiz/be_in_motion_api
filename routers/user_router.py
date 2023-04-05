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
        return {"msg": "success", "data": {}}
    else:
        return {"msg": "error", "data": {}}


@router.delete("/by-id/{id_user}",
               summary="Delete data from user by id_user",
               description="Delete data from user by id_user",
               response_description="Deletes data",
               response_model=schemes.user_schemes.UserDeleteResponse,
               operation_id="DeleteUserDataByIdUser"
               )
async def delete_user(user_id: str):
    return {"msg": "success", "data": {}}
