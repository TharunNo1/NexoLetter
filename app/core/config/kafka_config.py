from pydantic_settings import BaseSettings

class KafkaSettings(BaseSettings):
    BOOTSTRAP_SERVERS: str 
    TOPIC_SEND_NEWSLETTER: str 
    