# Sentiment Analysis of Conversation Surrounding Covid-19 Vaccine 

***

For our final project at Zip Code Wilmington, we chose to create a sentiment anlayis on the conversation on Twitter surrounding the COVID-19 vaccine in the United States. We produced streams of all the tweets using the Twitter API and Apache Airflow and put the data into an AWS SQL database. We then cleaned the data with Spark and returned it to the database.

After acquiring this data, we used NLTK machine learning models to analyze the sentiment of the tweets. We then separated tweets into four different tables, based on what region of the United States they came from and created various visualizations of the data using Wordcloud, Matplotlib, and Tableau (see below).

---  
In the sentiment analysis, tweets were split into three categories: positive, negative and neutral. Using Word Cloud, we generated images of the key words found in **positive** tweets. The larger the word, the more common it was:

<img src = "Images/positive-words.png">

Here are key words found in **negative** tweets:

<img src = "Images/negative-words.png">

This last Word Cloud has words found in **nuetral** tweets:

<img src = "Images/neutral-words.png">

Using Matplotlib, we made a stacked bar graph comparing the different regions in the United States:

<p align="center">
<img width="400" src = "Images/stackedbar-matplotlib.png">
</p>

And the whole process was automated using an Apache Airflow DAG:

<img src = "Images/dag.png">

Lastly, we made [interactive data visualizations using Tableau](https://public.tableau.com/profile/lee.givhan#!/vizhome/USASentimentViz1/Dashboard1?publish=yes)

### API Used  

- [Twitter's Streaming API](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data)
 
### Frameworks Used  

- Airflow
- AWS lightsail MySql
- PANDAS 
- Matplotlib
- Tableau
- NLTK
- Papermill
- PySpark

Here is a flowchart showing how all of the technologies worked together:

<img src = "Images/Twitter-Sentiment-Flow-Chart.jpeg">

## Meet the Team
---
### Anusha Jangalapalli
[Connect on LinkedIn](https://www.linkedin.com/in/anushajangalapalli/)   
  
### Lee Givhan  
[Connect on LinkedIn](https://www.linkedin.com/in/leegivhan/) 

### Sumalatha Konjeti
[Connect on LinkedIn](https://www.linkedin.com/in/sumalatha-konjeti/)
