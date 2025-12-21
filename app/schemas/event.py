from datetime import datetime
from uuid import uuid4, UUID
from pydantic import BaseModel, Field

class BaseEvent(BaseModel):
    event_id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    version: str = "v1"

class NewsletterDispatchEvent(BaseEvent):
    newsletter_id: int 
    template_id: str 
    recipient_group: str
