from typing import Optional
from pydantic import BaseModel, Field


class UserGetResponse(BaseModel):
    """
    User get response scheme
    """
    msg: str
    data: object = {}

