from pydantic import BaseModel, PositiveInt, Field
from typing import Optional, List
# import uuid


class Order(BaseModel):
    # id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid1()))
    order_id: str  
    pizza_type: str  
    size: str
    quantity: PositiveInt
    is_delivery: bool 
    special_instructions: Optional[str] = None  
    status: Optional[str] = None
    allergies_flaged: bool = False 

class Orders(BaseModel):
    orders: List[Order] = []