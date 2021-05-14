from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 5, 14),
    'end_date': datetime(2021, 5, 15),
    'depends_on_past': False,
    'email': ['system@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'my_first_dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1)
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag
)

templated_command = """"
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{macros.ds_add(ds, 7)}}"
    echo "{{params.my_param}}"
    {% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in '},
    dag=dag
)

t1 >> t2 >> t3
