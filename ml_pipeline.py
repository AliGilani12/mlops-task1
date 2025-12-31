from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

dag = DAG(
    'ml_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

preprocess = BashOperator(
    task_id='preprocess',
    bash_command='docker build -f Dockerfile.preprocess -t iris-preprocess . && docker run --rm iris-preprocess',
    dag=dag
)

train = BashOperator(
    task_id='train',
    bash_command='docker build -f Dockerfile.train -t iris-train . && docker run --rm iris-train',
    dag=dag
)

deploy = BashOperator(
    task_id='deploy',
    bash_command='docker build -f Dockerfile.serve -t iris-serve . && docker run -d -p 8000:8000 iris-serve',
    dag=dag
)

preprocess >> train >> deploy
