from fastapi import APIRouter, HTTPException
import core.schemes as schemes
import internal


router = APIRouter()

@router.get("/by-id/{id_user}",
            summary="Return info of physiotherapeut",
            description="Return info of physiotherapeut",
            response_description="Return info of physiotherapeut",
            response_model=schemes.physiotherapeut_info_schemes.PhysiotherapeutInfoGetResponse,
            operation_id="GetDataUserByIdUser"
            )
async def service(id_user: str):
    validate = internal.validate_uuid.is_uuid_valid(id_user)
    if validate is True:
        return {"msg": "success", "data":{}}
    else:
        return {"msg": "error", "data": {}}