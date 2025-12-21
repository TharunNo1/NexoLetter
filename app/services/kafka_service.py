from confluent_kafka.admin import AdminClient, NewTopic
from app.core.config import settings
from app.integrations.kafka.producer import KafkaProducer

class KafkaService:
    def __init__(self):
        self.producer = KafkaProducer(settings.kafka.BOOTSTRAP_SERVERS)
        self.admin: AdminClient | None = None

    def start(self):
        self.producer.start()
        self.admin = AdminClient({"bootstrap.servers": settings.kafka.BOOTSTRAP_SERVERS})

    def stop(self):
        self.producer.stop()

    async def ensure_topic(self):
        topic = NewTopic(
            topic=settings.kafka_topic_newsletter,
            num_partitions=3,
            replication_factor=1,
        )
        fs = self.admin.create_topics([topic])
        for _, f in fs.items():
            try:
                f.result()
            except Exception:
                pass  # Topic exists or broker handled it

    def send_newsletter(self, newsletter_id: str, content: dict, newsletter_topic: str):
        self.producer.produce(
            topic=newsletter_topic,
            key=newsletter_id,
            value={"newsletter_id": newsletter_id, "content": content},
        )

