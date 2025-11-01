# import
from fastapi import FastAPI
from app.schemas import Order
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
def startup():
    global orders
    orders = generate_orders(10)


@app.get("/")
def read_root():
    return orders
