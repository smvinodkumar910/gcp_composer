'''
Initial DAT to test the environment.
'''

from airflow import models
from airflow.operators import python
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
    dag_id='My First composer test',
    start_date=datetime.datetime(2021,1,1),
    schedule_interval=datetime.timedelta(hours=1)) as dag :

       pythonTenTimes = printTenTimes()
       pythonFiveTimes = printFiveTimes()

       pythonFiveTimes >> pythonTenTimes

