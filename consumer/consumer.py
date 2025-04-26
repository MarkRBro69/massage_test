from kafka import KafkaConsumer
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
TOPIC_NAME = os.getenv("KAFKA_TOPIC", "comments")


def main():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='comments-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    logger.info(f"Listening to Kafka topic '{TOPIC_NAME}'...")

    for message in consumer:
        data = message.value
        logger.info(f"Received message: {data}")


if __name__ == "__main__":
    main()
