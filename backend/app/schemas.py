from pydantic import BaseModel
from datetime import datetime


class Order(BaseModel):
  id: int
  order_number: str
  customer_name: str
  amount: int
  status: str
  created_at: datetime
