

from pydantic.fields import Field
from pydantic_settings import BaseSettings

class DbSettings(BaseSettings):
    DATABASE_URL: str = Field(default=None, alias="URL", nullable=False)
    ECHO: bool = False