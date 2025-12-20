from fastapi.openapi.models import EmailStr
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True