from kafka import KafkaProducer
import json
import os

KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL', 'kafka:9092')


def send_comment_created_event(comment_id, text, user_id):
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    event = {
        'type': 'comment_created',
        'comment_id': comment_id,
        'text': text,
        'user_id': user_id
    }
    producer.send('comments', value=event)
    producer.flush()
