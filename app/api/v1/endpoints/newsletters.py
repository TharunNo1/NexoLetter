from app.core.config import settings
from app.api.dependencies import NewsletterServiceDep
from fastapi import APIRouter, status

router = APIRouter(prefix="/newsletter", tags=["newsletters"])


@router.post("/send", status_code=status.HTTP_202_ACCEPTED)
def send_newsletter(
    newsletter_id: str,
    newsletter_service: NewsletterServiceDep,
):
    newsletter_topic = settings.kafka.TOPIC_SEND_NEWSLETTER
    newsletter_service.send_newsletter(newsletter_id, newsletter_topic)
    return {"status": "queued"}


@router.post("/generate")
async def generate_newsletter_content(
    newsletter_topic: str,
    newsletter_service: NewsletterServiceDep,
):
    newsletter_id = newsletter_service.generate_newsletter(newsletter_topic=newsletter_topic)
    return {"status": "queued", "newsletter_id": str(newsletter_id)}
