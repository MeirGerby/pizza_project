from typing import List

from db.mongodb_connection import get_collection
from schemas.order_schema import Order
from producer import send_data
from core.config import settings





def insert_one_order(data: dict) :
    collection = get_collection(settings.COLLECTION_NAME)
    insert_data = collection.insert_one(data)
    if data['_id']:
        data['_id'] = str(data['_id'])
    send_to_kafka = send_data(data)
    if insert_data:
        return insert_data
    return None

def create_logs(data, insert_data):
    return f"""insert data {data}, id: {insert_data.inserted_id}"""

def insert_orders(orders: List[Order]):
    logs = []
    for i in orders:
        inseted_data = insert_one_order(i.model_dump())
        log = create_logs(i, inseted_data)
        logs.append(log)
    return logs

def get_orders(order_id):
    collection = get_collection(settings.COLLECTION_NAME)
    return collection.find(filter={'order_id': order_id}, projection={"_id":0})
