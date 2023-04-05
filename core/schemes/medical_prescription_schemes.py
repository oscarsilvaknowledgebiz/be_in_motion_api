from typing import Optional
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null



class MedicalPrescriptionGetResponse(BaseModel):
    """
    User get response scheme
    """
    msg: str
    data: object = {}