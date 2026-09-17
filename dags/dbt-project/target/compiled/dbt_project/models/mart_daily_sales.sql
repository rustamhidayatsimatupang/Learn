

select
    date as sales_date,
    count(id) as total_transactions,
    sum(revenue) as total_revenue
from "airflow"."public"."stg_transactions"
group by 1