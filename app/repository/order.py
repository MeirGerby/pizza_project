from typing import List

from db.mongodb_connection import get_collection
from schemas.order_schema import Order
from producer import send_data

COLLECTION_NAME = 'orders'



def insert_one_order(data: dict):
    collection = get_collection(COLLECTION_NAME)
    insert_data = collection.insert_one(data)
    if data['_id']:
        data['_id'] = str(data['_id'])
    send_to_kafka = send_data(data)
    return f"""insert data {data}, id: {insert_data.inserted_id}"""


def insert_orders(orders: List[Order]):
    logs = []
    for i in orders:
        log = insert_one_order(i.model_dump())
        logs.append(log)
    return logs

def get_orders(order_id):
    collection = get_collection(COLLECTION_NAME)
    return collection.find(filter={'order_id': order_id}, projection={"_id":0})
