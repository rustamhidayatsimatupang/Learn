{{ config(materialized='view') }}

select
    transaction_id as id,
    transaction_date::date as date,
    product as product_name,
    amount::numeric as revenue
from {{ ref('raw_transactions') }}
