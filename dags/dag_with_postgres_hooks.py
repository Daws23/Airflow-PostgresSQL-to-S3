import csv
import logging

from datetime import timedelta, datetime
from tempfile import NamedTemporaryFile

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

default_args = {
    'owner': 'Mark',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

def postgres_to_S3(ds_nodash, next_ds_nodash):
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from orders where date >= %s and date < %s"
                   ,(ds_nodash, next_ds_nodash))
    
    with NamedTemporaryFile(mode='w', suffix=f"{ds_nodash}") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        f.flush()
        cursor.close()
        conn.close()
        logging.info("Saved orders data in text file: %s", f"dags/get_orders_{ds_nodash}.txt")

        s3_hook = S3Hook(aws_conn_id="minio_conn")
        s3_hook.load_file(
            filename=f.name,
            key=f"orders/{ds_nodash}.txt",
            bucket_name="airflow",
            replace=True
        )
        logging.info("Orders file %s has been pushed to S3!", f.name)

with DAG(
    dag_id = 'dag_with_prostgres_hooks_v2',
    default_args = default_args,
    start_date = datetime(2024, 3, 5),
    schedule_interval = '0 0 * * *',
) as dag:
    task1 = PythonOperator(
        task_id="poastgres_to_s3",
        python_callable=postgres_to_S3
    )

    task1