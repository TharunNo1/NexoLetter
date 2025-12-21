import json
from confluent_kafka import Producer

class KafkaProducer:
    def __init__(self, bootstrap_servers: str):
        self.producer: Producer | None = None 
        self.bootstrap_servers = bootstrap_servers
    
    def start(self):
        if self.producer is not None:
            return
        self.producer = Producer(
            {
                "bootstrap.servers": self.bootstrap_servers,
                "acks": "all",
            }
        )
    
    def stop(self):
        if self.producer:
            self.producer.flush(timeout=5.0)
        self.producer = None
    
    def produce(self, topic: str, key: str, value: dict, callback = None):
        if not self.producer:
            raise RuntimeError("Initialize Producer before publishing topics...")
        self.producer.produce(
            topic=topic,
            key=key,
            value=json.dumps(value),
            on_delivery=callback or self._default_callback,
        )
        self.producer.poll(1)
        self.producer.flush()
    
    def _default_callback(self, err, msg):
        if err is not None:
            print(f"Delivery failed for {msg.key()}: {err}")