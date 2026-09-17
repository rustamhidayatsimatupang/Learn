
  create view "airflow"."public"."stg_transactions__dbt_tmp"
    
    
  as (
    

select
    transaction_id as id,
    transaction_date::date as date,
    product as product_name,
    amount::numeric as revenue
from "airflow"."public"."raw_transactions"
  );