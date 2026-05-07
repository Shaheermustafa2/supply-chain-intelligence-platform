----------ON TIME DELIVERY %----------
select ( 100 *
    sum(
        case
            when status = 'On Time'
            then 1
            else 0
        end
    ) /
    count(*) ) as otif_percentage
from fact_shipments;

----------DELAY RATE %----------
select ( 100 *
    sum(
        case
            when status = 'Delayed'
            then 1
            else 0
        end
    ) /
    count(*) ) as delay_rate
from fact_shipments;

----------SUPPLIER'S PERFORMANCE----------
select
s.supplier_name,
count(*) as total_shipments,

round( avg(f.delay_days),
    2 ) as average_delay_days

from fact_shipments f

join dim_supplier s
on f.supplier_id = s.supplier_id

group by s.supplier_name

order by average_delay_days desc;

----------FREIGHT COST BY CATEGORY----------
select
p.category, sum(f.shipping_cost) as freight_cost

from fact_shipments f

join dim_product p
on f.product_id = p.product_id

group by p.category

order by freight_cost desc;

----------WAREHOUSE UTILIZATION----------
select
w.warehouse_name,
( 100 *
    sum(f.quantity) /
    w.capacity
    ) as utilization_percent

from fact_shipments f

join dim_warehouse w
on f.warehouse_id = w.warehouse_id

group by
w.warehouse_name,
w.capacity

order by utilization_percent desc;


