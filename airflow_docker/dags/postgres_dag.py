from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 4, 22)
}

with DAG('postgres_hello_world',
         default_args=default_args,
         schedule_interval=None) as dag:
    hello_world_query = """
        SELECT 1
    """

    hello_world_task = PostgresOperator(
        task_id='hello_world_task',
        postgres_conn_id='test',  # replace with your connection id
        sql=hello_world_query
    )

    hello_world_task