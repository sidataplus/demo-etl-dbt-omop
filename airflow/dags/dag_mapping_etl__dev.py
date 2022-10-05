import datetime
import json

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# /opt/airflow/includes/dbt

dbt_dir = "/opt/airflow/includes/dbt"
dbt_profile = dbt_dir + "/profile"
dbt_project = dbt_dir + "/prod"

custom_args = {
    'retries': 5,
    'retry_delay': timedelta(seconds=5),
}

dag = DAG(
    dag_id='dag_mapping_etl__dev',
    start_date= datetime.now(),
    #start_date= datetime(2022, 7, 9)
    description='A dbt wrapper for Airflow',
    #schedule_interval=timedelta(days=1),
    schedule_interval="@once",
    default_args=custom_args
)

def load_manifest():
    local_filepath = f"{dbt_profile}/manifest.json"
    with open(local_filepath) as f:
        data = json.load(f)

    return data

def make_dbt_task(node, dbt_verb):
    """Returns an Airflow operator either run and test an individual model"""
    model = node.split(".")[-1]

    dbt_task = BashOperator(
        task_id=f"dbt_transform__{model}",
        bash_command=f"""
        dbt run --profiles-dir {dbt_profile} --project-dir {dbt_project} --models {model} --log-path /opt/airflow/dbt_logs
        """,
        # bash_command=f"""
        # python -c 'from dbt.main import main; main()' run --profiles-dir {dbt_profile} --project-dir {dbt_project} --models {model}
        # """,
        dag=dag,
    )

    return dbt_task


data = load_manifest()

dbt_tasks = {}
for node in data["nodes"].keys():
    if node.split(".")[0] == "model":
        #if data["nodes"][node]["config"]["tags"] != "mapping":
        if "mapping" in data["nodes"][node]["config"]["tags"]:
            #node_test = node.replace("model", "test")
            dbt_tasks[node] = make_dbt_task(node, "run")
            #dbt_tasks[node_test] = make_dbt_task(node, "test")

for node in data["nodes"].keys():
    if node.split(".")[0] == "model":
        #if data["nodes"][node]["config"]["tags"] != "mapping":
        #if next(iter(data["nodes"][node]["config"]["tags"] or []), None) != "mapping":
        if "mapping" in data["nodes"][node]["config"]["tags"]:
            # Set dependency to run tests on a model after model runs finishes
            #node_test = node.replace("model", "test")
            #dbt_tasks[node] >> dbt_tasks[node_test]

            # Set all model -> model dependencies
            for upstream_node in data["nodes"][node]["depends_on"]["nodes"]:
                upstream_node_type = upstream_node.split(".")[0]
                if upstream_node_type == "model":
                    if "mapping" in data["nodes"][upstream_node]["config"]["tags"]:
                        dbt_tasks[upstream_node] >> dbt_tasks[node]