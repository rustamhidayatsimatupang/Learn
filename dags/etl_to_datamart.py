from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 6, 28),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'dag_isi_data_mart',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    # 1. Task untuk Membuat Tabel
    create_table = PostgresOperator(
        task_id='create_table_task',
        postgres_conn_id='postgres_data_mart', # Sesuai dengan ID di Connections
        sql="""
        CREATE TABLE IF NOT EXISTS data_mart.penjualan (
            id SERIAL PRIMARY KEY,
            produk VARCHAR(100),
            jumlah INT,
            tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    # 2. Task untuk Memasukkan Data
    insert_data = PostgresOperator(
        task_id='insert_data_task',
        postgres_conn_id='postgres_data_mart',
        sql="""
        INSERT INTO data_mart.penjualan (produk, jumlah) VALUES 
        ('Laptop', 1),
        ('Mouse', 5),
        ('Keyboard', 3);
        """
    )

    create_table >> insert_data
