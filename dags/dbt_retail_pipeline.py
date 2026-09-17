from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'data_engineer',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    'dbt_retail_pipeline',
    default_args=default_args,
    schedule_interval='0 2 * * *',
    catchup=False,
    tags=['dbt', 'sales'],
) as dag:

    load_seed = BashOperator(
        task_id='dbt_seed',
        bash_command='cd /opt/airflow/dags/dbt-project && dbt seed --profiles-dir /opt/airflow/dags/dbt-project'
    )

    transform_data = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/dags/dbt-project && dbt run --select +mart_daily_sales --profiles-dir /opt/airflow/dags/dbt-project'
    )

    load_seed >> transform_data
