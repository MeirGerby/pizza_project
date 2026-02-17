import json

from confluent_kafka import Consumer
from db.mongodb_connection import get_collection
from db.redis_connection import get_redis_connection 
from utils import search_words, convert_to_upper
from core.config import settings


def create_consumer():
    CONSUMER_CONFIG = {
        "bootstrap.servers": "kafka:9092",
        "group.id": "text-team",
        "auto.offset.reset": "earliest"
    }

    return Consumer(CONSUMER_CONFIG)  # type: ignore

def get_data():
    consumer = create_consumer()
    consumer.subscribe(["pizza-orders"])
    mongo_coll = get_collection(settings.COLLECTION_NAME)
    redis_connection = get_redis_connection()
    print("Consumer is running and subscribed to text-orders topic")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("Error:", msg.error())
                continue

            value = msg.value().decode("utf-8")  # type: ignore
            if search_words(value): 
                list_text = convert_to_upper(value)
                clean_text = " ".join(list_text)
                order = json.loads(value)
                order_id = order.get('order_id')
                print(f"Received order: {order}") 

                mongo_coll.update_one(
                    {'order_id': order_id} ,
                    {'$set': {'allergies_flaged': 'true', 'protocol_cleaned': clean_text}}
                    )
                redis_connection.delete(order_id)


    except KeyboardInterrupt:
        print("Stopping consumer")

    finally:
        consumer.close()

get_data()
