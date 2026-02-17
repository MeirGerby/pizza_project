from db.redis_connection import get_redis_connection


def exist_in_cache(key: str) -> bool:
    """checks if the value is exists in redis chache"""
    conn = get_redis_connection()
    return bool(conn.exists(key))

def get_order_by_id(order_id):
    conn = get_redis_connection()
    return conn.get(order_id)   

def insert_data_to_redis(key: str, data):
    conn = get_redis_connection()
    return conn.set(key, data,ex=3600)
    