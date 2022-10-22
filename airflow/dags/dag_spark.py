import airflow
from datetime import datetime, timedelta
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    'start_date': datetime(2020, 11, 18)
}
with airflow.DAG('dag_teste_spark',
                  default_args=default_args,
                  schedule_interval=None) as dag:
    task_elt_documento_pagar = SparkSubmitOperator(
        task_id='extract_postgresql',
        conn_id='spark_default',
        application="plugins/spark_jobs/postgres_extract.py",
        packages="org.postgresql:postgresql:42.5.0"
    )