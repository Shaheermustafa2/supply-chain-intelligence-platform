----------MONTHLY DELIVERY TREND----------
select extract(
    month from order_date ) as month,
round ( avg(delay_days), 2) as average_delay
from fact_shipments
group by month
order by month;

----------SUPPLIERS REGION RISK----------
select s.region,
count(*) as shipments,
round(
    avg(f.delay_days),2) as average_delay
from fact_shipments f
join dim_supplier s on f.supplier_id = s.supplier_id
group by s.region
order by average_delay desc;

----------CATEGORY WISE DELAY----------
select p.category, count(*) as shipments,
round(
    avg(f.delay_days),2 ) as average_delay
from fact_shipments f
join dim_product p on f.product_id = p.product_id
group by p.category
order by average_delay desc;

-----------TOP 10 DELAYED SUPPLIERS----------
select s.supplier_name, count(*) as delayed_shipments
from fact_shipments f
join dim_supplier s on f.supplier_id = s.supplier_id
where f.status = 'Delayed'
group by s.supplier_name
order by delayed_shipments desc
limit 10;

----------HIGH VOLUME PRODUCTS----------
select p.product_name, sum(f.quantity) as total_units
from fact_shipments f
join dim_product p on f.product_id=p.product_id
group by p.product_name
order by total_units desc
limit 10;

----------SUPPLIER RATING & DELAY----------
select s.supplier_rating,
round( avg(f.delay_days), 2) as average_delay
from fact_shipments f
join dim_supplier s
on f.supplier_id = s.supplier_id
group by s.supplier_rating
order by s.supplier_rating;