<h2> 1- Scope of the Project </h2>
In this Udacity Data Engineering Nanodegree Capstone Project, I have built a data pipeline which includes various technology and processes. The main idea under this project is to create a data model for Business Intelligence Applications. Business Intelligence Applications always need a well designed data model. Also this data model can easily be used for analytics especially machine learning model.
<br>

<h2> 2- About Data </h2>
In this project, I have used food.com Recipes and Reviews datasets from Kaggle. You can see the details of the datasets <a href="https://www.kaggle.com/irkaal/foodcom-recipes-and-reviews">here</a>. <br><br>
<b> The recipes dataset: </b> It contains 522,517 recipes from 312 different categories. This dataset provides information about each recipe like cooking times, servings, ingredients, nutrition, instructions, and more. Recipe dataset is in csv format and it has 28 columns. The columns are ;
<ul>
<li>RecipeId</li>
<li>Name</li>
<li>AuthorId</li>
<li>AuthorName</li>
<li>CookTime</li>
<li>PrepTime</li>
<li>TotalTime</li>
<li>DatePublished</li>
<li>Description</li>
<li>Images</li>
<li>RecipeCategory</li>
<li>Keywords</li>
<li>RecipeIngredientQuantities</li>
<li>RecipeIngredientParts</li>
<li>AggregatedRating</li>
<li>ReviewCount</li>
<li>Calories</li>
<li>FatContent</li>
<li>SaturatedFatContent</li>
<li>CholesterolContent</li>
<li>SodiumContent</li>
<li>CarbohydrateContent</li>
<li>FiberContent</li>
<li>SugarContent</li>
<li>ProteinContent</li>
<li>RecipeServings</li>
<li>RecipeYield</li>
<li>RecipeInstructions</li>
</ul>

Sample data is shown below.<br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/recipes.jpg">

<b> The reviews dataset: </b> It contains 1,401,982 reviews from 271,907 different users. This dataset provides information about the author, rating, review text, and more. Reviews dataset is in parquet format and it has 8 columns. The columns are ;
<ul>
<li>ReviewId</li>
<li>RecipeId</li>
<li>AuthorId</li>
<li>AuthorName</li>
<li>Rating</li>
<li>Review</li>
<li>DateSubmitted</li>
<li>DateModified</li>
</ul>

Sample data is shown below.<br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/reviews.jpg">

<h2> 3- Data Exploration </h2>
There were some data quality issues in original datasets as shown below. 
<ul>
  <li><b>Missing Values: </b> There were missing values in each datasets. I deleted the rows which contain missing values in important columns like ReviewId, AuthorId, RecipeCategory, DateSubmitted. </li>
  <li><b>Duplicate Data: </b> There were duplicate data in each sets. I deleted the duplicate data before data modelling.</li>
</ul>

<h2> 4- Definition of Data Model </h2>

<b> Redshift Staging Tables </b>
<img src="https://github.com/lemarc58/udacity/blob/main/image/staging_tables.jpg" style="float:left;vertical-align:bottom">
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

<h2> 7- Possible Scenarios </h2>
<ul>
  <li><b>If the data was increased by 100x. =></b> In this case, I would prefer to use Spark on Amazon EMR Cluster. Because it has high processing capability.</li>
  <li><b>If the pipelines were run on a daily basis by 7am. =></b> It is enough to change schedule_interval value and set it to daily 7 am in Airflow.</li>
  <li><b>If the database needed to be accessed by 100+ people. =>/<b> Amazon Redshift has enough resource to serve for many people but in case of any performance issues, I can scale up Redshift cluster. </li>
</ul>		
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
