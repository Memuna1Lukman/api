from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime,date



class UserApi(BaseModel):
    id : Optional[int] = None
    api_keys :  Optional[str] = None
    name: str


class ResponseApi(BaseModel):
    id : Optional[int] = None
    api_keys :  Optional[str] = None
    name: str
    date : Optional[datetime] = None

    model_config = {"from_attributes": True}


class TimingLimit(BaseModel):
    id : Optional[int] = None
    api_keys :  Optional[str] = None
    created_at : Optional[datetime] = None