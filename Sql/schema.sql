create database star_schema_data_warehouse;

create table dim_supplier (
    supplier_id int primary key,
    supplier_name text,
    region text,
    lead_time_days int,
    supplier_rating numeric
);

create table dim_warehouse (
    warehouse_id int primary key,
    warehouse_name text,
    city text,
    state text,
    capacity int
);

create table dim_product (
    product_id int primary key,
    product_name text,
    category text,
    unit_cost numeric,
    reorder_level int
);

create table dim_date (
    full_date date primary key,
    month int,
    quarter int,
    year int
);

create table fact_shipments (
    shipment_id int primary key,

    supplier_id int,
    warehouse_id int,
    product_id int,

    order_date date,

    quantity int,

    shipping_cost numeric,

    delay_days int,

    status text,

    foreign key (supplier_id)
    references dim_supplier(supplier_id),

    foreign key (warehouse_id)
    references dim_warehouse(warehouse_id),

    foreign key (product_id)
    references dim_product(product_id)
);