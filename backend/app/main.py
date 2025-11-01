# import
from fastapi import FastAPI
from app.schemas import User
from app.data_generator import generate_users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
origins = [
  "http://localhost:5173",
  "https://qiu1996.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["GET"],
)



users = []


@app.on_event("startup")
def startup():
    global users
    users = generate_users(10)


@app.get("/")
def read_root():
    return users
