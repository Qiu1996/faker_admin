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
def get_orders(page: int = 1, page_size: int = 10):
  start = (page - 1) * page_size
  end = start + page_size
  return {
    "data": orders[start:end],
    "total": len(orders),
  }
