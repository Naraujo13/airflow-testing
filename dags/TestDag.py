from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# Definindo alguns argumentos básicos
default_args = {
  'owner': 'Nícolas de Araujo',
  'depends_on_past': False,
  'start_date': datetime(2019, 10, 2)
}

dag = DAG(
  'TestDag',
  catchup=False,
  schedule_interval=timedelta(minutes=1),
  default_args=default_args
)

t1 = BashOperator(
  task_id='first_etl',
  bash_command="""
  cd $AIRFLOW_HOME/dags/etl_scripts/
  python3 first_script.py
  """,
  dag=dag
)

t2 = BashOperator(
  task_id='second_etl',
  bash_command="""
  cd $AIRFLOW_HOME/dags/etl_scripts/
  python3 second_script.py
  """,
  dag=dag
)

t1 >> t2
