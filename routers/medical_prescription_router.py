from fastapi import APIRouter, HTTPException
import core.schemes as schemes
import internal


router = APIRouter()

@router.get("/by-id/{id_user}",
            summary="Return medical prescription data by id_user",
            description="Return medical prescription data by id_user",
            response_description="Returns medical prescription",
            response_model=schemes.medical_prescription_schemes.MedicalPrescriptionGetResponse,
            operation_id="GetDataUserByIdUser"
            )
async def service(id_user: str):
    validate = internal.validate_uuid.is_uuid_valid(id_user)
    if validate is True:
        return {"msg": "success", "data":{}}
    else:
        return {"msg": "error", "data": {}}