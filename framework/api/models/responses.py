from pydantic import BaseModel, ConfigDict, Field


class BaseApiModel(BaseModel):
    model_config = ConfigDict(strict=True, extra="ignore")


class BaseResponse(BaseApiModel):
    response_code: int = Field(alias="responseCode")


class MessageResponse(BaseResponse):
    message: str


class UserDetails(BaseApiModel):
    name: str
    email: str
    title: str
    birth_day: str
    birth_month: str
    birth_year: str
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str


class UserResponse(UserDetails):
    id: int = Field(gt=0)


class UserAccountResponse(BaseResponse):
    user: UserResponse
