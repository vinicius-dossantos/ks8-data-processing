
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'datamasterylab',
    'start_date': datetime(year=2025, month=1, day=15),
    'catchup': False
}

dag = DAG(
    dag_id='hello_world',
    default_args=default_args,
    schedule=timedelta(days=1)
)

t1 = BashOperator(
    task_id='hello_world',
    bash_command='echo "Hello World"',
    dag=dag
)

t2 = BashOperator(
    task_id='hello_dml',
    bash_command='echo "Hello Data Mastery Lab"',
    dag=dag
)