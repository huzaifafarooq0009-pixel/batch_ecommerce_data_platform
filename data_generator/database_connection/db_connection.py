from sqlalchemy import create_engine
DB_USER = "postgres"
DB_PASS = "erroR999"
DB_HOST = "Localhost"
DB_PORT = "5432"
DB_NAME = "batch_ecommerce"
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
def test_connection():
    try:
        with engine.connect() as connection:
            print("Connection to the database was succesful")
    except Exception as e:
            print("connection to the database failed")

if __name__ == "__main__":
    test_connection()