from pydantic_settings.main import SettingsConfigDict
from fastapi.openapi.models import EmailStr
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    model_config = SettingsConfigDict(from_attributes=True)