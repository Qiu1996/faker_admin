from faker import Faker
from app.schemas import User

fake = Faker('en_US')  # 或 'en_US'

def generate_users(count: int = 100):
    return [
        User(
            id=i,
            name=fake.name()
        )
        for i in range(1, count + 1)
    ]
