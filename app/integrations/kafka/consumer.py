from app.models import KafkaEvent
from app.core.database import SessionLocal
from sqlalchemy.orm.session import Session
import uuid
import json
from confluent_kafka import Consumer, KafkaError
from abc import ABC, abstractmethod

class KafkaConsumer(ABC):

    def __init__(self, bootstrap_servers: str, group_id: str):
        self.consumer: Consumer | None = None 
        self.consumer_id = None
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topics = []
    
    def start(self):
        if self.consumer is not None:
            return
        self.consumer_id = uuid.uuid4()
        self.consumer = Consumer({
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": self.group_id,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False
        })
        if self.topics:
            self.consumer.subscribe(self.topics)
    
    @abstractmethod
    def handle_event(self, db: Session, key: str, data: dict):
        pass

    def _execute_safe_flow(self, message):
        event_key = message.key().decode('utf-8') if message.key() else None
        if not event_key: 
            return

        with SessionLocal() as db:
            if db.query(KafkaEvent).filter_by(event_key=event_key).first():
                self.consumer.commit(message)
                return

            try:
                data = json.loads(message.value().decode('utf-8'))
                self.handle_event(db, data, event_key)
                db.add(KafkaEvent(event_key=event_key))
                db.commit()
                self.consumer.commit(message)
            except Exception as e:
                db.rollback()
                print(f"Failed to process {event_key}: {e}")
    
    def stop(self):
        if self.consumer:
            self.consumer_id = None
            self.consumer.close()
        self.consumer = None
    
    def subscribe(self, topic: str):
        if topic not in self.topics:
            self.topics.append(topic)
    
    def run(self):
        if not self.topics:
            print("No topics subscribed. Exiting...")
            return
        try:
            self.start()
            while True:
                message = self.consumer.poll(1.0)
                if message is None:
                    continue 
                if message.error():
                    if message.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    print(f"Error in consumer message: {message.error()}")
                self._execute_safe_flow(message)
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()