import airflow
from airflow import DAG
import os
import papermill as pm
import pandas as pd
from datetime import datetime,timedelta
#import papermill as pm
#from airflow.operators.papermill_operator import PapermillOperator
from airflow.operators.python_operator import PythonOperator

# from airflow.executors import
# def read_files():
#     df = pd.read_csv("/Users/suma/Tennis_project/Stats.csv")


def call_jupyter_twitterdata_mysql():
    pm.execute_notebook(
        '/Users/suma/ZCW-FinalProject/Gathering_Cleaning_TwitterData/Inserting_TwitterData_AWSMysql.ipynb',
        '/Users/suma/ZCW-FinalProject/Output_Files/Output_Inserting_TwitterData_AWSMysql.ipynb',
        parameters=dict(TEST=True,
                        QUICK_RUN=True, ), )

def call_jupyter_cleaning_storing():
    pm.execute_notebook(
        '/Users/suma/ZCW-FinalProject/Gathering_Cleaning_TwitterData/Cleaning_Storing_TwitterData.ipynb',
        '/Users/suma/ZCW-FinalProject/Output_Files/Output_Cleaning_Storing_TwitterData.ipynb',
        parameters=dict(TEST=True,
                        QUICK_RUN=True, ), )

def call_jupyter_twitter_sentiment_analysis():
    pm.execute_notebook(
        '/Users/suma/ZCW-FinalProject/Sentiment_Analysis/Twitter_SentimentAnalysis.ipynb',
        '/Users/suma/ZCW-FinalProject/Output_Files/Output_Twitter_SentimentAnalysis.ipynb',
        parameters=dict( TEST=True,
                         QUICK_RUN=True,), )
def call_jupyter_twitter_visualization():
    pm.execute_notebook(
        '/Users/suma/ZCW-FinalProject/Sentiment_Analysis/Sentiment_Analysis_visualization.ipynb',
        '/Users/suma/ZCW-FinalProject/Output_Files/Output_Sentiment_Analysis_visualization.ipynb',
        parameters=dict( TEST=True,
                         QUICK_RUN=True,), )

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021,1,11),
    'retries': 0,
    # 'retry_delay': timedelta(minutes=5),

}
# dag = DAG(dag_id='DAG_2',default_args=default_args,catchup=False,schedule_interval='@once')
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
#
# t3b = PythonOperator(
#      task_id='read_and_clean_news_data',
#      provide_context=False,
#      python_callable=call_jupyter_news,
#      dag=dag,
# )

t1 >> t2 >> t3 >> t4
# t1 >> t3b