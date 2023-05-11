from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

import logging


def print_log(**kwargs):
    logger = logging.getLogger("airflow.task")
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')


with DAG(
    'hello_world',
    description='A simple DAG for checking infrastructure',
    start_date=datetime(2023, 2, 1),
    schedule_interval=timedelta(hours=1),
    tags=['temp'],
) as dag:
    t = PythonOperator(
        task_id="print_to_log",
        python_callable=print_log
    )

t
print('b')

if __name__ == '__main__':
    dag.cli()
