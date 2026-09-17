{{ config(materialized='table') }}

select
    date as sales_date,
    count(id) as total_transactions,
    sum(revenue) as total_revenue
from {{ ref('stg_transactions') }}
group by 1
