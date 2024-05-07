from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Mark',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id = 'our_first_dag',
    default_args = default_args,
    description = 'This is my first of DAGs',
    start_date = datetime(2024, 3, 7, 2),
    schedule_interval = '0 0 * * *',
) as dag:
    task = BashOperator(
        task_id='task_1',
        bash_command="echo Hello World, this is the first task!",
    )
    task
