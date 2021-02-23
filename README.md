About Project
In this project, I built a data pipeline from S3 to Redshift. I am collecting the data from S3 bucket and then I am inserting it into staging tables in Redshift. After some data transformations, all the data in staging tables is being loaded into dimension tables. Finally I put some data quality check rules for data in dimension tables. 
Whole ETL pipeline is defined in Airflow.

<b> Graph View of the DAG </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow.jpg">
<br>

<b> Gantt View of the DAG </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow_gantt.jpg">
<br>

<b> Tree View of the DAG </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow_tree.jpg">
<br>

<b> Architecture of the Project </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/architecture.jpg">
<br>

<b> S3 tables </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/s3.jpg">
<br>

<b> Redshift Staging Tables </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/staging_tables.jpg">
<br>

<b> Redshift Fact and Dimension Tables </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/fact_dimension_tables.jpg">
<br>


About Data
Log data => Log data of application
Song data => Real Song data


Project Directory
create_all_tables.sql => sql queries for creating staging, fact and dimension tables  
udac_example_dag.py => main dag file
sql_queries.py => sql queries for inserting data into tables
data_quality.py => check data quality operator file
load_dimension.py => load dimension tables operator file
load_fact.py => load fact table operator file
stage_redshift.py => load staging tables operator file


How to run project
1- Start airflow (/opt/airflow/start.sh)
2- Create AWS and Redshift connections in Airflow
3- Activate DAG
4- Control log then Enjoy :)
