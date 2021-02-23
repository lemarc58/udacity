<h2> 1- Scope of the Project </h2>
<br><br>

<h2> 2- About Data </h2>
<br><br>

<h2> 3- Data Exploration </h2>
<br><br>

<h2> 4- Definition of Data Model </h2>

<b> Redshift Staging Tables </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/staging_tables.jpg">
<br>
<b> Redshift Fact and Dimension Tables </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/fact_dimension_tables.jpg">
<br>
<br><br>

<h2> 5- ETL Process </h2>
<b> Graph View of the DAG </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow.jpg">
<br>
<b> Gantt View of the DAG </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow_gantt.jpg">
<br>
<b> Tree View of the DAG </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow_tree.jpg">
<br>
<b> S3 tables </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/s3.jpg">
<br>
<br><br>

<h2> 6- Architecture of the Project </h2>
<b> Architecture of the Project </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/architecture.jpg">
<br>
<br><br>

<h2> 7- Scenarios </h2>
    If the data was increased by 100x.
		If the pipelines were run on a daily basis by 7am.
		If the database needed to be accessed by 100+ people.
<br><br>


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
