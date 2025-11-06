# import
from fastapi import FastAPI
from app.schemas import OrderList
from app.data_generator import generate_orders
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

# CORS
origins = ["http://localhost:5173", "https://qiu1996.github.io"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
)


orders = []


@app.on_event("startup")
def init_data():
    global orders
    orders = generate_orders()


@app.get("/order", response_model=OrderList)
def get_orders(
  page: int = 1,
  page_size: int = 10,
  sortBy: str = "created_at",
  sort: str = "descending",
  status: Optional[str] = None,
  search: Optional[str] = None,
  date: Optional[str] = None,
  amount: Optional[str] = None
):

  result = orders

  if status:
    status_list = status.split(',')
    result = [order for order in result if order.status in status_list]

  if search:
    result = [
      order for order in result if search in order.order_number or search in order.customer_name
    ]

  if date:
    [date_start, date_end] = date.split(',')
    result = [
      order for order in result if date_start <= order.created_at <= date_end
    ]

  if amount:
    [amount_min, amount_max] = amount.split(',')
    amount_min = int(amount_min)
    amount_max = int(amount_max) if amount_max != "Infinity" else float('inf')
    result = [
      order for order in result if amount_min <= order.amount <= amount_max
    ]

  reverse = (sort == "descending")
  result = sorted(result, key=lambda order: getattr(order, sortBy), reverse=reverse)

  start = (page - 1) * page_size
  end = start + page_size
  return {
    "data": result[start:end],
    "total": len(result),
  }
