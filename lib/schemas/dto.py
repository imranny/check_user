from typing import Optional
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(..., description="User name", example="Imran")
    age: int = Field(..., gt=0, lt=120, description="User age", example=15)
    sex: Optional[str] = Field(None, description = "User gender", example = 'male')
    job: Optional[str]  = Field(None, description="User job", example="developer")


class UserReturn(UserCreate):
    id: int = Field(..., description="Auto-generated ID", example=1)
    name: str
    age: int
    sex: Optional[str]
    job: Optional[str]


class UserResponse(BaseModel):
    success: bool
    user: UserReturn

