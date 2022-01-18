'''
Initial DAT to test the environment.
'''

from airflow import models
from airflow.operators import python
from airflow.utils import dates
import datetime


def printTenTimes():
    i=0
    while(i<=10):
        print('value of i is :{}'.format(i))
        i=i+1

def printFiveTimes():
    i=0
    while(i<=5):
        print('value of i is :{}'.format(i))
        i=i+1

with models.DAG(
    dag_id='learning_dags',
    start_date=dates.days_ago(0),
    schedule_interval=datetime.timedelta(hours=1)) as dag :

    pythonTenTimes = python.PythonOperator(python_callable=printTenTimes, task_id='test10')
    pythonFiveTimes = python.PythonOperator( python_callable=printFiveTimes,  task_id='test5')
    
    pythonFiveTimes >> pythonTenTimes

