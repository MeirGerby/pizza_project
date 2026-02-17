from fastapi import File, UploadFile, APIRouter
import json 

from services.order import orders_service, get_orders
from services.redis_service import exist_in_cache, get_order_by_id, insert_data_to_redis


route = APIRouter() 

@route.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File()):
    data = await file.read()
    order = orders_service(data)
    return order
       
@route.get("/order/{order_id}")
async def get_order(order_id: str):
    if exist_in_cache(order_id):
        order = get_order_by_id(order_id)
        order_data = json.loads(order)  # type: ignore
        return {"source": "redis_cache", "data": order_data}
    else:
        order = get_orders(order_id)
        if order:
            order_str = json.dumps(list(order))
            insert_data_to_redis(order_id, order_str)
            return {"source": "mongodb", "data": order_str}