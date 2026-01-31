# File: data_generator/generate/batch/data_base.py
from datetime import datetime
from faker import Faker
import pandas as pd
import random
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# ------------------- PostgreSQL Connection -------------------
# Make sure to replace these with your actual credentials
engine = create_engine(
    "postgresql+psycopg2://postgres:erroR999@localhost:5432/batch_ecommerce",
    echo=True  # Prints SQL statements for debugging
)

# ------------------- Faker Setup -------------------
fake = Faker()

# ------------------- Generate Customers -------------------
customers = []
for i in range(1, 100000):
    customers.append([
        i,
        fake.name(),
        fake.email(),
        fake.country(),
        fake.date_between(start_date="-2y", end_date="today")
    ])

customers_df = pd.DataFrame(customers, columns=["customer_id", "name", "email", "country", "signup_date"])

# ------------------- Generate Products -------------------
products = []
categories = ["Electronics", "Clothing", "Sports", "Home"]
for i in range(1, 5000):
    products.append([
        i,
        fake.word().capitalize(),
        random.choice(categories),
        round(random.uniform(10, 500), 2)
    ])

products_df = pd.DataFrame(products, columns=["product_id", "product_name", "category", "price"])

# ------------------- Generate Orders -------------------
orders = []
for i in range(1, 200000):
    orders.append([
        i,
        random.randint(1, 100),  # customer_id
        random.randint(1, 50),   # product_id
        fake.date_between(start_date="-1y", end_date="today"),
        random.randint(1, 5)     # quantity
    ])

orders_df = pd.DataFrame(orders, columns=["order_id", "customer_id", "product_id", "order_date", "quantity"])

# ------------------- Insert into PostgreSQL -------------------
def insert_to_postgres(df, table_name):
    try:
        df.to_sql(table_name, engine, if_exists="replace", index=False, method='multi')  # method='multi' speeds up insertion
        print(f"✅ {table_name} inserted successfully with {len(df)} rows!")
    except SQLAlchemyError as e:
        print(f"❌ Error inserting {table_name}: {e}")

# Insert all tables
insert_to_postgres(customers_df, "customers_raw")
insert_to_postgres(products_df, "products_raw")
insert_to_postgres(orders_df, "orders_raw")

print("🎉 All raw data has been generated and inserted into PostgreSQL successfully!")
