import pandas as pd
import numpy as np
import os
os.makedirs("data", exist_ok=True)
np.random.seed(42)

# ----------Suppliers----------
suppliers = pd.DataFrame({
    "supplier_id": range(1, 51),
    "supplier_name": [
        f"Supplier_{i}"
        for i in range(1, 51)
    ],
    "region": np.random.choice(
        ["North", "South", "East", "West"],
        50
    ),
    "lead_time_days": np.random.randint(
        2, 15, 50
    ),
    "supplier_rating": np.round(
        np.random.uniform(
            3.0, 5.0, 50
        ),
        1
    )
})


# ----------Warehouses----------
warehouses = pd.DataFrame({
    "warehouse_id": range(1, 11),
    "warehouse_name": [
        f"WH_{i}"
        for i in range(1, 11)
    ],
    "city": np.random.choice(
        [
            "Mumbai",
            "Delhi",
            "Bangalore",
            "Hyderabad"
        ],
        10
    ),
    "state": np.random.choice(
        [
            "MH",
            "DL",
            "KA",
            "TS"
        ],
        10
    ),
    "capacity": np.random.randint(
        5000,
        15000,
        10
    )
})


suppliers.to_csv(
    "data/suppliers.csv",
    index=False
)

warehouses.to_csv(
    "data/warehouses.csv",
    index=False
)

# ----------Products----------
categories = [
    "Electronics",
    "Furniture",
    "Apparel",
    "Groceries",
    "Medical",
    "Automotive",
    "Sports",
    "Beauty"
]

products = pd.DataFrame({
    "product_id": range(1, 1001),
    "product_name": [
        f"Product_{i}"
        for i in range(1, 1001)
    ],
    "category": np.random.choice(
        categories,
        1000
    ),
    "unit_cost": np.round(
        np.random.uniform(50, 5000, 1000),
        2
    ),
    "reorder_level": np.random.randint(
        20, 200, 1000
    )
})

products.to_csv(
    "data/products.csv",
    index=False
)


# ----------Shipments----------
shipment_count = 150000

order_dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31"
)

shipment_dates = np.random.choice(
    order_dates,
    shipment_count
)

dispatch_dates = (
    pd.to_datetime(shipment_dates)
    + pd.to_timedelta(
        np.random.randint(
            1, 4, shipment_count
        ),
        unit="D"
    )
)

estimated_dates = (
    dispatch_dates
    + pd.to_timedelta(
        np.random.randint(
            3, 8, shipment_count
        ),
        unit="D"
    )
)

actual_dates = (
    estimated_dates
    + pd.to_timedelta(
        np.random.randint(
            -2, 5, shipment_count
        ),
        unit="D"
    )
)

shipments = pd.DataFrame({
    "shipment_id": range(
        1,
        shipment_count + 1
    ),

    "supplier_id": np.random.randint(
        1, 51,
        shipment_count
    ),

    "warehouse_id": np.random.randint(
        1, 11,
        shipment_count
    ),

    "product_id": np.random.randint(
        1, 1001,
        shipment_count
    ),

    "order_date": shipment_dates,

    "dispatch_date": dispatch_dates,

    "estimated_delivery_date": estimated_dates,

    "actual_delivery_date": actual_dates,

    "quantity": np.random.randint(
        1, 200,
        shipment_count
    ),

    "shipping_cost": np.round(
        np.random.uniform(
            100, 5000,
            shipment_count
        ),
        2
    )
})


shipments["status"] = np.where(
    shipments["actual_delivery_date"]
    <= shipments["estimated_delivery_date"],
    "On Time",
    "Delayed"
)

shipments.to_csv(
    "data/shipments.csv",
    index=False
)

print("data generated successfully.")