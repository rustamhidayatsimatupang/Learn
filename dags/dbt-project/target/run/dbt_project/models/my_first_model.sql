
  create view "postgres"."public"."my_first_model__dbt_tmp" as (
    select 
    1 as id,
    'Airflow & dbt Integration' as title,
    current_timestamp as created_at
  );
