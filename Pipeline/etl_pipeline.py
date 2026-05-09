import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# ----------Database connection----------
conn = psycopg2.connect(
    host="localhost",
    database="star_schema_data_warehouse",
    user="postgres",
    password="password"
)

cursor = conn.cursor()

# ----------loading----------
def load_table(df, table_name):
    query = f"""
        INSERT INTO {table_name}
        VALUES %s
        ON CONFLICT DO NOTHING
    """

    execute_values(cursor, query, df.values.tolist())
    print(f"{table_name} loaded")

suppliers = pd.read_csv("data/suppliers.csv")
warehouses = pd.read_csv("data/warehouses.csv")
products = pd.read_csv("data/products.csv")

load_table(suppliers, "dim_supplier")
load_table(warehouses, "dim_warehouse")
load_table(products, "dim_product")

shipments = pd.read_csv("data/shipments.csv")

shipments["order_date"] = pd.to_datetime(shipments["order_date"])

dates = shipments[["order_date"]].drop_duplicates()
dates.columns = ["full_date"]

dates["month"] = dates["full_date"].dt.month
dates["quarter"] = dates["full_date"].dt.quarter
dates["year"] = dates["full_date"].dt.year

load_table(dates, "dim_date")

shipments["estimated_delivery_date"] = pd.to_datetime(
    shipments["estimated_delivery_date"]
)

shipments["actual_delivery_date"] = pd.to_datetime(
    shipments["actual_delivery_date"]
)

shipments["delay_days"] = (
    shipments["actual_delivery_date"]
    - shipments["estimated_delivery_date"]
).dt.days

fact_shipments = shipments[
    [
        "shipment_id",
        "supplier_id",
        "warehouse_id",
        "product_id",
        "order_date",
        "quantity",
        "shipping_cost",
        "delay_days",
        "status"
    ]
]

load_table(fact_shipments, "fact_shipments")

cursor.execute("SELECT COUNT(*) FROM fact_shipments")
count = cursor.fetchone()[0]

print(f"Fact rows loaded: {count}")

conn.commit()
cursor.close()
conn.close()

print("ETL completedd")
