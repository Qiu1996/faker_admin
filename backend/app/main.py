# import
from fastapi import FastAPI
from app.schemas import OrderList
from app.data_generator import generate_orders
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from datetime import datetime

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
  sort_by: str = "created_at",
  sort: str = "descending",
  status: Optional[str] = None,
  search: Optional[str] = None,
  date_start: Optional[str] = None,
  date_end: Optional[str] = None,
  amount: Optional[str] = None
):
  result = apply_filter(orders, status, search, date_start, date_end, amount)
  result = apply_sort(result, sort_by, sort)
  paginated = apply_pagination(result, page, page_size)

  return {
    "data": paginated,
    "total": len(result),
  }

def apply_filter(orders, status, search, date_start, date_end, amount):
  result = orders

  if status:
    status_list = status.split(',')
    result = [order for order in result if order.status in status_list]

  if search:
    result = [
      order for order in result if search in order.order_number or search in order.customer_name
    ]

  if date_start and date_end:
    date_start = datetime.fromisoformat(date_start.replace('Z', '')).replace(tzinfo=None)
    date_end = datetime.fromisoformat(date_end.replace('Z', '')).replace(tzinfo=None)

    result = [
      order for order in result if date_start <= datetime.strptime(order.created_at, '%Y-%m-%d %H:%M:%S') <= date_end
    ]

  if amount:
    [amount_min, amount_max] = amount.split(',')
    amount_min = int(amount_min)
    amount_max = int(amount_max) if amount_max != "Infinity" else float('inf')
    result = [
      order for order in result if amount_min <= order.amount <= amount_max
    ]
  return result

def apply_sort(orders, sort_by, sort):
  reverse = (sort == "descending")
  result = sorted(orders, key=lambda order: getattr(order, sort_by), reverse=reverse)
  return result

def apply_pagination(orders, page, page_size):
  start = (page - 1) * page_size
  end = start + page_size
  return orders[start:end]
