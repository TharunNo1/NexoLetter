from pydantic.fields import Field
from pydantic_settings import BaseSettings

class DbSettings(BaseSettings):
    DATABASE_URL: str = Field(default=None, alias="URL", json_schema_extra={
        "nullable": False
    })
    ECHO: bool = False