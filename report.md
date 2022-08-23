"""
@author: 21076682
Task 6. A short report in Markdown format (<1000 words) reflecting on the assignment, the problems encountered and the solutions found.
In addition you should discuss and outline some of the Python tools and libraries that could be used to visualize this data. What maps / charts with which content?
You should also briefly outline the Learning Outcomes you have managed to achieve in undertaking this Assignment.

"""

>#Introduction

This evaluation of air quality was conducted at various locations throughout the United Kingdom. Measurement of air quality, levels of different airborne contaminants such as Nitrogen Monoxide (NO), Nitrogen Dioxide (NO2), and particulate matter (also known as particle pollution) are all significant contributors to the overall air quality index. Pollution of the air can be harmful and detrimental to the environment, plants, livestock and human health. The information was gathered from 18 monitoring stations in the United Kingdom.
The  Assessment was based on Understanding data cleansing, normalization, and sharding processes by writing python
scripts to process and convert a dataset called Bristol air quality data to first (cleansed) CSV and then (normalized) SQL and then insert the (normalized) SQL into a SQL Server database. the report is also to find a suitable python library that can be used to visualize the data using the bristol air quality datasets
To achieve the goal of this Reflection report, The Approach for the evaluation was solved using pandas to achieve the objective of this Reflection paper. Pandas is a Python library of rich data structures and resources for working with organized data sets used in statistics, finance, social sciences, and various other fields. The library provides integrated, intuitive routines for performing joint data manipulations and analysis on such data sets.
Finally, the data was modelled and imported to a NoSQL database model called MongoDB.


PROBLEMS ENCOUNTERED AND SOLUTION FOUND
- I experienced low System performance / Low memory warning. The reason for this low_memory warning was because Pandas tried to determine what datatype to set by analyzing the data in each column and guessing datatypes for each column is very memory demanding so I set low_memory = false and dtype=str this read the entire csv as a string irrespective of the datatype. Then silences the error message, but this does not actually change anything else it only stops the warning trigger.

- When populating the database with the python scripts thats takes 700k+ csv file as input, I noticed long runtime that ultimately resulted in poor performance of the Database. the database was timing out. then i decided to insert the record iteratively, by creating a while loop that inserts the record from index 0 to 999th record which means it will continously insert 1000 record at every loop to the current value, then it goes back into te loop and continues until the next iteration of 1 is more than the record of the csv file.

- During creation of table I assigned double to the column called geo_point 2 and gave it a lenght 30, it was observed that it record failed to insert into that column, so i changed the data type assigned varchar to it, i did this to ensure that i adhered to following the rule of Data integerity constraints 

 
 
> Discuss and outline some of the  Python tools and libraries that could be used to visualize this data. What maps / charts with which content?

Data visualisation is a critical component of data analysis. After all, there's no easier way to grasp the data's secret patterns and layers than to see them represented visually! (GeeksforGeeks, 2021). Below are some of the python tools and libraries that could be used to visualize this data
  
### Python tools and libraries and Types of Plots
In Data Science,  Python is one of the most popular programming languages for data analytics as well as data visualization. And there many libraries and tools that can create complex and meaningful data visualisation. 
Therefore, this piece will briefly discussion these tools and relevant charts and maps that can be applied in the case in study.

#### Pandas library: 
The pandas library is one the python libraries installed as a package to read data in any dataframe for data analysis and manipulation. It is an open source, fast, flexible, and built on top of python programming language. It will be useful in reading this data which has been written in a csv file for data wrangling. 

#### Matplotlib: 
This is the foremost and widely used data visualization library with 2-D plotting feature of Python, released in 2003. For example, we can show the relationship among the pollutants using the line plots, scatterplot or take the mean of the reading over the period of time using the histogram, pie chart or bar chart. 

#### Seaborn: 
Seaborn is a Python data visualization library that is based on Matplotlib and closely integrated with the NumPy and pandas data structures. We can use a simple pie chart or multiple bar chart to show content such as high, moderate, or low against the pollutants.

#### GGplot: 
This is similar with the ggplot2 in R, which a powerful API for data visualisation using python script. We can show a multiple bar chart of the pollutants across the stations over 5years whilst the layers will be annualised.

#### Bokeh: 
Bokeh is a python library with interactive visualisation which can be created in HTML files with web connectivity features and supports streaming of real-time data. The air pollutants can be mapped against the hourly reading presented in graphical manner using some of python scripts.

#### Plotly: 
This is a python library that can also be for data visualisation and it can be embedded in web applications. In the given case, we can plot for connect data gaps contour graph to show any missing values in the parameters.  
#### Geoplotlib: 
Unlike most of python libraries for data visualisation, the Geoplotlib is basically a python library for data that can map geographical data. In the given case, we can visualise the measure of air pressure of the respective stations (location with Bristol) in form of a geographical maps for further analysis.

LEARNING GOALS AND OUTCOMES

1. I learned how to Combine, join, or merge data sets that has something in common, for easy data analysis

2. I learnt I need to have my submission files and my dataset in the same directory for my scripts to be able to run.

3. By writing python scripts I got insight on how to clean up, and filter off unwanted records to have a clean data 

4. After completing the evaluation, I discovered that the pandas.to sql feature, which was my initial solution, is not suitable for such massive inserts into a SQL Server database, It was very slow it took almost an hour for the application to complete Unlike Mysql which was only about 4 minutes when using mysql database.

5. I learned how to construct and execute a series of SQL queries to extract data using various filters and constraints.

6. I learned about nosql database management system. Particularly Mongodb which I used in my work. I also got insight on how some other nosql database systems works.

7. I created a relational database (MySQL) and then wrote a Python script to Insert the SQL into the required tables, ensuring that all the relationship between tables are met.

8. I Learned how To Map (forward engineer) a table in a SQL database in Third Normal form, This Third normal  is about partially eliminating dependencies in a table with one to many relationship

9. I Learned how to use the MARKDOWN 

> REFERENCES
www.mongodb.com
https://fetstudy.uwe.ac.uk/~p-chatterjee/2021-22/modules/dmf-jan/assignment/
https://www.w3schools.in/benefits-of-using-nosql
https://www.youtube.com/watch?v=WBUN_4NWHYI
https://stackoverflow.com/