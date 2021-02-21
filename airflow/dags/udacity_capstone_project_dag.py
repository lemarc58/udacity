from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (PostgresOperator, StageToRedshiftOperator, LoadFactOperator, LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

#Default arguments for DAG
default_args = {
    'owner': 'udacity_data_engineering_nanodegree',
    'start_date': datetime(2020, 2, 19),
    'depends_on_past': False,
    'email_on_retry': True
}

#Definition of DAG
dag = DAG('udacity_capstone_project',
          default_args=default_args,
          description='Udacity Data Engineering Nanodegree Capstone Project',
          schedule_interval='@once',
          max_active_runs=1
        )

#start_operator Task by using DummyOperator
start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

#create_all_tables Task by using PostgresOperator
create_all_tables = PostgresOperator(
    task_id="create_all_tables",
    dag=dag,
    postgres_conn_id="redshift",
    sql="create_all_tables.sql"
)

#stage_reviews_to_redshift Task by using StageToRedshiftOperator
stage_reviews_to_redshift = StageToRedshiftOperator(
    task_id='stage_reviews_to_redshift',
    dag=dag,
    table="staging_reviews",
    s3_bucket='udacity-food/reviews',
    s3_key='reviews',
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    provide_context=True
)

#stage_recipes_to_redshift Task by using StageToRedshiftOperator
stage_recipes_to_redshift = StageToRedshiftOperator(
    task_id='stage_recipes_to_redshift',
    dag=dag,
    table="staging_recipes",
    s3_bucket='udacity-food/recipes',
    s3_key='recipes',
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    file_type='csv',
    provide_context=True
)

#load_reviews_table Task by using LoadFactOperator
load_reviews_table = LoadFactOperator(
    task_id='load_reviews_table',
    dag=dag,
    table='reviews',
    sql=SqlQueries.reviews_table_insert,
    redshift_conn_id='redshift',
    provide_context=True
)

#load_author_dimension_table Task by using LoadDimensionOperator
load_author_dimension_table = LoadDimensionOperator(
    task_id='load_author_dimension_table',
    dag=dag,
    table='author',
    sql=SqlQueries.author_table_insert,
    redshift_conn_id='redshift',
    provide_context=True
)

#load_category_dimension_table Task by using LoadDimensionOperator
load_category_dimension_table = LoadDimensionOperator(
    task_id='load_category_dimension_table',
    dag=dag,
    table='category (RecipeCategory)',
    sql=SqlQueries.category_table_insert,
    redshift_conn_id='redshift',
    provide_context=True
)

#load_recipes_dimension_table Task by using LoadDimensionOperator
load_recipes_dimension_table = LoadDimensionOperator(
    task_id='load_recipes_dimension_table',
    dag=dag,
    table='recipes',
    sql=SqlQueries.recipes_table_insert,
    redshift_conn_id='redshift',
    provide_context=True
)

#load_time_dimension_table Task by using LoadDimensionOperator
load_time_dimension_table = LoadDimensionOperator(
    task_id='load_time_dimension_table',
    dag=dag,
    table='time',
    sql=SqlQueries.time_table_insert,
    redshift_conn_id='redshift',
    provide_context=True
)

#run_quality_checks_author Task by using DataQualityOperator
run_quality_checks_author = DataQualityOperator(
    task_id='run_quality_checks_author',
    dag=dag,
    redshift_conn_id='redshift',
    query='select count(*) from author where AuthorId is null;',
    result=0,
    provide_context=True
)

#run_quality_checks_recipes Task by using DataQualityOperator
run_quality_checks_recipes = DataQualityOperator(
    task_id='run_quality_checks_recipes',
    dag=dag,
    redshift_conn_id='redshift',
    query='select count(*) from recipes where Name is null;',
    result=0,
    provide_context=True
)

#end_operator Task by using DummyOperator
end_operator = DummyOperator(task_id='End_execution',  dag=dag)

#Dependicies of Tasks
start_operator >> create_all_tables >> [stage_reviews_to_redshift, stage_recipes_to_redshift] >> load_reviews_table
load_reviews_table >> [load_author_dimension_table, load_time_dimension_table] >> run_quality_checks_author
load_reviews_table >> load_category_dimension_table >> load_recipes_dimension_table >> run_quality_checks_author >> run_quality_checks_recipes
run_quality_checks_recipes >> end_operator