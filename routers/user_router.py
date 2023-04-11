from fastapi import APIRouter, HTTPException, Response, status
import core.schemes as schemes
import internal


router = APIRouter()


@router.get("/by-id/{id_user}",
            summary="Return data of user by id_user",
            description="Return data of user by id_user",
            response_description="Returns basic data from user",
            response_model=schemes.user_schemes.UserGetResponse,
            operation_id="GetDataUserByIdUser"
            )
async def service(response: Response, id_user: str):
    validate = internal.validate_uuid.is_uuid_valid(id_user)
    if validate is True:
        return {"msg": "success", "data":{}}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg": "error", "data": "This ID is invalid"}


@router.put("/info",
            summary="Updates user data by id_user",
            description="Updates user data by id_user",
            response_description="Updates user",
            response_model=schemes.user_schemes.UserInfoPutResponse,
            operation_id="UpdateUserDataByIdUser"
            )
async def update_user(response: Response, user: schemes.user_schemes.UserInfoPut):
    validate = internal.validate_uuid.is_uuid_valid(user.id_user)
    if validate is True:
        return {"msg": "success", "data": {}}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg": "error", "data": {}}



@router.post("",
             summary="Creates a new user by id_user",
             description="Creates a new user by id_user",
             response_description="Creates a new user",
             response_model=schemes.user_schemes.UserCreateResponse,
             operation_id="CreateUserByIdUser"
             )
async def create_user(response:Response, user: schemes.user_schemes.UserPost):
    return {"msg": "success", "data": {}}