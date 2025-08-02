from typing import Optional

from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., gt=0, description="Unique user ID", example=1)
    name: str = Field(..., description="name", example="Imran")
    age: int = Field(..., gt=0, lt=120, description="age", example=15)
    job: Optional[str]  = Field(None, description="job info", example="Developer")

class UserResponse(BaseModel):
    success: bool
    user: User

