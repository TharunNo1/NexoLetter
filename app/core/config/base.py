from app.core.config.security import AuthSettings
from app.core.config.database import DbSettings
from app.models.enums import Environment
from pydantic_settings.main import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    ENVIRONMENT: Environment
    LOG_LEVEL: str

    API_V1_STR: str

    db: DbSettings
    auth: AuthSettings

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == Environment.PRODUCTION
    

    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore",
        env_nested_delimiter="__"
    )

settings = Settings()
