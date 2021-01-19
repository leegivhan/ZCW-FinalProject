import airflow
from airflow import DAG
import os
import papermill as pm
import pandas as pd
from datetime import datetime,timedelta
from airflow.models import Variable
#import papermill as pm
#from airflow.operators.papermill_operator import PapermillOperator
from airflow.operators.python_operator import PythonOperator


var_list = Variable.get("sentiment_analysis_variables", deserialize_json=True)
Inserting_TwitterData_AWSMysql = var_list["Inserting_TwitterData_AWSMysql"]
Output_Inserting_TwitterData_AWSMysql = var_list["Output_Inserting_TwitterData_AWSMysql"]
Cleaning_Storing_TwitterData = var_list["Output_Cleaning_Storing_TwitterData"]
Output_Cleaning_Storing_TwitterData = var_list["Output_Cleaning_Storing_TwitterData"]
Twitter_SentimentAnalysis = var_list["Twitter_SentimentAnalysis"]
Output_Twitter_SentimentAnalysis = var_list["Output_Twitter_SentimentAnalysis"]
Sentiment_Analysis_visualization = var_list["Sentiment_Analysis_visualization"]
Output_Sentiment_Analysis_visualization = var_list["Output_Sentiment_Analysis_visualization"]

def call_jupyter_twitterdata_mysql():
    pm.execute_notebook(
        Inserting_TwitterData_AWSMysql,
       Output_Inserting_TwitterData_AWSMysql,
        parameters=dict(TEST=True,
                        QUICK_RUN=True, ), )

def call_jupyter_cleaning_storing():
    pm.execute_notebook(
        Cleaning_Storing_TwitterData,
        Output_Cleaning_Storing_TwitterData,
        parameters=dict(TEST=True,
                        QUICK_RUN=True, ), )

def call_jupyter_twitter_sentiment_analysis():
    pm.execute_notebook(
        Twitter_SentimentAnalysis,
        Output_Twitter_SentimentAnalysis,
        parameters=dict( TEST=True,
                         QUICK_RUN=True,), )
def call_jupyter_twitter_visualization():
    pm.execute_notebook(
        Sentiment_Analysis_visualization,
        Output_Sentiment_Analysis_visualization,
        parameters=dict( TEST=True,
                         QUICK_RUN=True,), )

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021,1,11),
    'retries': 0,
    # 'retry_delay': timedelta(minutes=5),

}

dag = DAG(
    dag_id='Sentiment_Analysis_Twitter_Data',
    default_args=default_args,
    description='twitter and new data',
    # schedule_interval=timedelta(days=1),
)
t1 = PythonOperator(
     task_id='get_twitterdata_mysql',
     provide_context=False,
     python_callable=call_jupyter_twitterdata_mysql,
     dag=dag,
)
t2 = PythonOperator(
     task_id='get_cleaning_storing_data',
     provide_context=False,
     python_callable=call_jupyter_cleaning_storing,
     dag=dag,
)

t3 = PythonOperator(
     task_id='twitter_sentiment_analysis',
     provide_context=False,
     python_callable=call_jupyter_twitter_sentiment_analysis,
     dag=dag,
)
t4 = PythonOperator(
     task_id='twitter_visualization',
     provide_context=False,
     python_callable=call_jupyter_twitter_visualization,
     dag=dag,
)
t1 >> t2 >> t3 >> t4
