from app.core.database import Base
from sqlalchemy import Column, DateTime, String, Boolean, PrimaryKeyConstraint

class KafkaEvent(Base):

    __tablename__ = "kafka_events"

    event_key = Column(String, nullable=False)
    customer_id = Column(String, nullable=False)
    
    is_processed = Column(Boolean, default=True)
    processed_at = Column(DateTime(timezone=True))

    __table_args__ = (
        PrimaryKeyConstraint('event_key', 'customer_id', name='pk_event_customer'),
    )