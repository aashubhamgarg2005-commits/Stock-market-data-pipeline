from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
#from success_alert import success_alert
#from failure_alert import failure_alert
#from start_alert import job_start

"""
default_args = {
    "on_failure_callback":failure_alert
}
"""
with DAG(
    dag_id="stock_market_batch_pipeline",
    start_date=datetime(2026,8,9),
    schedule="@daily",
    catchup=False
) as dag:

    #start = job_start()


    extract = BashOperator(
        task_id="extract_data",
        bash_command="cd /opt/stock-market-data && docker compose up rest-producer"
    )

    transform = BashOperator(
        task_id="batch_processing",
        bash_command= (
            "docker compose "
        "-f /opt/stock-market-data/docker-compose.yml "
        "up spark-batch"
        )
    )

    load = BashOperator(
        task_id="load_to_warehouse",
        bash_command="docker compose up loader"
    )

    #success = success_alert()

    extract>>transform>>load
