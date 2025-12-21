from app.core.database import Base
from sqlalchemy import Column, DateTime, String, PrimaryKeyConstraint, func

class ProcessedKafkaEvent(Base):

    __tablename__ = "processed_kafka_events"

    event_key = Column(String, nullable=False)
    group_id = Column(String, nullable=False)

    processed_at = Column(DateTime(timezone=True),server_default=func.now())

    __table_args__ = (
        PrimaryKeyConstraint('event_key', 'group_id', name='pk_event_consumer'),
    )