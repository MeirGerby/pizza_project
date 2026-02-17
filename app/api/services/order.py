import json
from typing import List
from schemas.order_schema import Order
from repository.order import insert_orders, get_orders


def create_order_schema(order: dict) -> Order:
    order['status'] = 'PREPARING'
    return Order(**order)

def create_orders(orders: bytes):
    orders_str = orders.decode('utf-8')
    orders_list: List[Order] = []
    for i in json.loads(orders_str):
        order_schema = create_order_schema(i)
        orders_list.append(order_schema)
    return orders_list
    

def orders_service(orders: bytes):
    orders_list = create_orders(orders)
    return insert_orders(orders_list)

def get_orders_service(order_id):
    return get_orders(order_id)