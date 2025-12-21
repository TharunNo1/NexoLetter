from app.core.config.kafka_config import KafkaSettings
from app.core.config.auth_config import AuthSettings
from app.core.config.db_config import DbSettings
from app.constants import Environment
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    ENVIRONMENT: Environment
    LOG_LEVEL: str

    API_V1_STR: str

    db: DbSettings
    auth: AuthSettings
    kafka: KafkaSettings

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == Environment.PRODUCTION
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore",
        env_nested_delimiter="__"
    )

