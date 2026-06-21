from datetime import datetime
import pandas as pd
from faker import Faker
from sqlalchemy import create_engine
import random
from sqlalchemy.exc import SQLAlchemyError

fake = Faker()

engine = create_engine(
    "postgresql+psycopg2://postgres:erroR999@localhost:5432/batch_ecommerce",
    echo=True
)

# ------------------- Customers -------------------

costumers = []

for i in range(1, 100000):
    costumers.append([
        i,
        fake.name(),
        fake.email(),
        fake.country(),
        fake.date_between(start_date="-5y", end_date="today")
    ])

customers_df = pd.DataFrame(
    costumers,
    columns=["id", "name", "email", "country", "signup_date"]
)

# ------------------- Products -------------------

product = []

categories = ["electronics", "clothing", "sports", "home"]

for i in range(1, 200000):
    product.append([
        i,
        fake.word().capitalize(),
        random.choice(categories),
        round(random.uniform(10, 500), 2)
    ])

product_df = pd.DataFrame(
    product,
    columns=["product_id", "product_name", "category", "price"]
)

# ------------------- Orders -------------------

orders = []

for i in range(1, 500000):
    orders.append([
        i,
        random.randint(1, 100),
        random.randint(1, 50),
        fake.date_between(start_date="-5y", end_date="today"),
        random.randint(1, 5)
    ])

orders_df = pd.DataFrame(
    orders,
    columns=["order_id", "customer_id", "product_id", "date", "quantity"]
)

# ------------------- Insert Function -------------------

def insert_to_postgres(df, table_name):
    try:
        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False,
            method="multi"
        )
        print(f"✅ {table_name} inserted successfully with {len(df)} rows!")

    except SQLAlchemyError as e:
        print(f"❌ Error inserting {table_name}: {e}")

# ------------------- Insert Data -------------------

insert_to_postgres(customers_df, "customers_raw")
insert_to_postgres(product_df, "products_raw")
insert_to_postgres(orders_df, "orders_raw")

print("🎉 All raw data has been generated and inserted into PostgreSQL successfully!")