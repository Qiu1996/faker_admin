from faker import Faker
from app.schemas import Order

fake = Faker('zh_TW')

def generate_orders(count: int = 10000):
    orders = []
    for i in range(1, count + 1):
      create_time = fake.date_time_between()
      data = {
        "id":i,
        "order_number": f"ORD{create_time.strftime('%Y%m%d%H%M%S')}",
        "customer_name": fake.name(),
        "amount": fake.random_int(min=1000, max=10000),
        "status": fake.random_element(elements=('pending', 'completed', 'cancelled')),
        "created_at": create_time.strftime('%Y-%m-%d %H:%M:%S'),
      }

      orders.append(Order(**data))
    orders.sort(key=lambda order: order.created_at, reverse=True)
    return orders
