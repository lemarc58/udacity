About Project
In this project, I built a data pipeline from S3 to Redshift. I am collecting the data from S3 bucket and then I am inserting it into staging tables in Redshift. After some data transformations, all the data in staging tables is being loaded into dimension tables. Finally I put some data quality check rules for data in dimension tables. 
Whole ETL pipeline is defined in Airflow.


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