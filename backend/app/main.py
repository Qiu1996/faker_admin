# import
from fastapi import FastAPI
from app.schemas import OrderList
from app.data_generator import generate_orders
from fastapi.middleware.cors import CORSMiddleware

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
  sort: str = "descending"
):

  reverse = (sort == "descending")
  sorted_orders = sorted(orders, key=lambda order: getattr(order, sortBy), reverse=reverse)

  start = (page - 1) * page_size
  end = start + page_size
  return {
    "data": sorted_orders[start:end],
    "total": len(sorted_orders),
  }
