# Sentiment Analysis of Conversation Surrounding Covid-19 Vaccine 

***

For our final project at Zip Code Wilmington, we chose to create a sentiment anlayis on the conversation surrounding the COVID-19 vaccine from the Twitter API. We produced streams of all the tweets using Apache Airflow, then analyzed the sentiment of the tweets and stored them in an AWS SQL database.

After acquiring this data, we used NLTK machine learning models to analyze the sentiment of the tweets. We then separated tweets into four different tables, based on what region of the United States they came from. 

We created various visualizations of the data using Matplotlib and Tableau, comparing the sentiment based on different regions of the United States (see below).


## Meet the Team
---
### Anusha Jangalapalli
[Connect on LinkedIn](https://www.linkedin.com/in/anushajangalapalli/) 
 
  - "Aspiring Data Engineer with a Masters in Computer Science, finding analytical solutions using latest technologies and languages(Python, SQL), frameworks(Pandas, Numpy, NLTK, flask, django), Databases (MySQL, Redis), Pipelines(Spark, Airflow, Kafka), Cloud Infrastructure(AWS S3), Visualization(Matplotlib, Seaborn, Bokeh) and tools(Jupiter, PyCharm, Spyder, Databricks). Also familiar with Docker and Kubernetes."  
  
### Lee Givhan  
[Connect on LinkedIn](https://www.linkedin.com/in/leegivhan/)

  - "Detailed Data Engineer seeking to use data analysis to guide well-informed business decisions. Former Home Depot Order Fulfillment Associate and touring musician. Studied Python and SQL. Created a blackjack game with a team of three utilizing Python and Github."  

### Sumalatha Konjeti
[Connect on LinkedIn](https://www.linkedin.com/in/sumalatha-konjeti/)

  - "Masters in Computer Applications from Osmania University, India. Former ABAP Developer. Constructed a web application for forums using python, Flask, and backed by a SQL database on a team of 6 - worked on Bootstrap UI and a "favorites" feature. Made a Tennis tournament pipeline using Airflow, Papermill and Jupyter notebook. Skills: Python, SQL, Pandas, Airflow, DAGs and Spark."
  
  
---  
### API Used  

- [Twitter's Streaming API](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data)
 
### Frameworks Used  

- Airflow
- PANDAS 
- Matplotlib
- Tableau
