from airflow import DAG
from airflow.decorators import task 
from datetime import datetime

with DAG(
    dag_id="dag_with_taskflow",
    start_date=datetime(2025,9,1),
    schedule='@once',
    catchup=False,
) as dag:
    @task
    def start():
        initial_number=10
        print(f"The number start with {initial_number}")
        return initial_number
    
    @task
    def add(number):
        number= number+2
        print(f"the number 2 added to {number}")
        return number
    
    @task
    def sub(number):
        number = number - 2
        print(f"the number is sub 2 {number}")
        return number
    @task
    def mult(number):
        number=number *2
        print(f"the number is multipied is 2 {number}")
        return number
    @task
    def squre(number):
        number=number^2
        print(f"the number squred is 2 {number}")
        return number
    start=start()
    add=add(start)
    sub=sub(add)
    mult=mult(sub)
    squre=squre(mult)




    