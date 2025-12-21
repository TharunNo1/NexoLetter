from pydantic_settings import BaseSettings
from pydantic import Field 

class AuthSettings(BaseSettings):
    SECRET_KEY: str = "super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MAX_LOGIN_ATTEMPTS: int = Field(default=5, ge=1)