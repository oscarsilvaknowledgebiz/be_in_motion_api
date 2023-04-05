from typing import Optional
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null



class UserGetResponse(BaseModel):
    """
    User get response scheme
    """
    msg: str
    data: object = {}


class UserUpdateResponse(BaseModel):
    """
    User update response scheme
    """
    msg: str
    data: object = {}


class UserCreateResponse(BaseModel):
    """
    User create response
    """
    msg: str
    data: object = {}


class UserPost(BaseModel):
    """
    User Post
    """
    _id: str
    name: str
    email: str
    password: Optional[str] = Field(default=null, alias="password")
    gmail_access_token: Optional[str] = Field(default=null, alias="gmailAccessToken")
    exponent_push_token: Optional[str] = Field(default=null, alias="exponentPushToken")
    picture: Optional[str] = Field(default=null, alias="picture")
    phone: Optional[str] = Field(default=null, max_length=11, alias="phone")
    birth_date: Optional[str] = Field(default=null, alias="birthDate", max_length=10)
    is_active: bool = Field(default=True, alias="isActive")
    is_admin: bool = Field(default=False, alias="isAdmin")
    is_verified: bool = Field(default=False, alias="isVerified")


class UserPut(BaseModel):
    """
    User Put
    """
    name: str
    password: Optional[str] = Field(default=null, alias="password")
    exponent_push_token: Optional[str] = Field(default=null, alias="exponentPushToken")
    picture: Optional[str] = Field(default=null, alias="picture")
    phone: Optional[str] = Field(default=null, max_length=11, alias="phone")
    birth_date: Optional[str] = Field(default=null, alias="birthDate", max_length=10)
    is_active: bool = Field(default=True, alias="isActive")
    is_admin: bool = Field(default=False, alias="isAdmin")
    is_verified: bool = Field(default=False, alias="isVerified")
