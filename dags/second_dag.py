from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello World")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 19),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval='45 12 * * *'
)

t1 = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)