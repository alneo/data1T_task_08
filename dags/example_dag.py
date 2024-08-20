from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

default_args = {
  'owner': 'airflow',
  'depends_on_past': False,
  'start_date': datetime(2023, 7, 19),
  'email_on_failure': False,
  'email_on_retry': False,
}

dag = DAG(
  'example_dag',
  default_args=default_args,
  description='A simple tutorial DAG',
  schedule=None,
)

t1 = EmptyOperator(
  task_id='dummy_task',
  retries=3,
  dag=dag,
)