from fastapi import FastAPI
from app.schemas import User
from app.data_generator import generate_users

app = FastAPI()

users = []


@app.on_event("startup")
def startup():
    global users
    users = generate_users(10)


@app.get("/")
def read_root():
    return users
