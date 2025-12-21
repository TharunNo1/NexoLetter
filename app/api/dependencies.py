from sqlalchemy.orm.session import Session
from app.services import KafkaService, NewsletterService, UserService
from typing import Annotated
from fastapi import Depends
from app.core.database import SessionLocal


def get_db():
    with SessionLocal() as db:
        yield db


def get_user_service(
    db=Depends(get_db),
):
    return UserService(db)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]


def get_kafka_service():
    kafka_service = KafkaService()
    kafka_service.start()
    yield kafka_service
    kafka_service.stop()


KafkaServiceDep = Annotated[KafkaService, Depends(get_kafka_service)]


def get_newsletter_service(
    db: Session = Depends(get_db),
    kafka: KafkaService = Depends(get_kafka_service),
):
    return NewsletterService(db, kafka)


NewsletterServiceDep = Annotated[NewsletterService, Depends(get_newsletter_service)]
