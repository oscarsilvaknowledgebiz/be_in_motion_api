from fastapi import APIRouter, HTTPException
import core.schemes as schemes
import internal


router = APIRouter()

@router.get("/by-id/{id_user}",
            summary="Return vinculation between user and physiotherapeut",
            description="Return vinculation between user and physiotherapeut",
            response_description="Returns vincultion between user and physiotherapeut",
            response_model=schemes.user_physiotherapeut_schemes.UserPhysiotherapeutGetResponse,
            operation_id="GetDataUserByIdUser"
            )
async def service(id_user: str):
    validate = internal.validate_uuid.is_uuid_valid(id_user)
    if validate is True:
        return {"msg": "success", "data":{}}
    else:
        return {"msg": "error", "data": {}}