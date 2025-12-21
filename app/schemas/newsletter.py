
from pydantic import BaseModel
class NewsletterSendRequest(BaseModel):
    newsletter_id: str 
    content: dict