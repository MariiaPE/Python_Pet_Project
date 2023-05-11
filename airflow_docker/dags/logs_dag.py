from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from helpers.helpers import process
import os

import logging
with DAG(
    'process',
    description='DAG for ETL logs',
    start_date=datetime(2023, 4, 5),
    schedule_interval=timedelta(days=1),
    tags=['logs'],
) as dag:
    t = PythonOperator(
        task_id="etl_logs",
        python_callable=process
    )

t


if name == 'main':
    dag.cli()