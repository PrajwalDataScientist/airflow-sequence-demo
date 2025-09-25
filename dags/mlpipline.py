from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Task functions
def preprocess_task():
    print("this preprocess")

def train_model():
    print("this is train_model")

def evaluate_model():
    print("this is evaluate the model")

# DAG definition
with DAG(
    "ml_pipeline",
    start_date=datetime(2025, 9, 25),
    schedule="@weekly",   # ✅ new keyword
    catchup=False,
) as dag:

    preprocess = PythonOperator(
        task_id="preprocess",
        python_callable=preprocess_task,
    )

    train = PythonOperator(
        task_id="training",
        python_callable=train_model,
    )

    evaluate = PythonOperator(
        task_id="evaluate",
        python_callable=evaluate_model,
    )

    # Dependencies
    preprocess >> train >> evaluate
