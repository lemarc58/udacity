<h2> 1- Scope of the Project </h2>
In this Udacity Data Engineering Nanodegree Capstone Project, I have built a data pipeline which includes various technology and processes. The main idea under this project is to create a data model for Business Intelligence Applications. Business Intelligence Applications always need a well designed data model. Also this data model can easily be used for analytics especially machine learning model.
<br>

<h2> 2- About Data </h2>
In this project, I have used food.com Recipes and Reviews datasets from Kaggle. You can see the details of the datasets <a href="https://www.kaggle.com/irkaal/foodcom-recipes-and-reviews">here</a>. <br><br>
<b> The recipes dataset: </b> It contains 522,517 recipes from categories. This dataset provides information about each recipe like cooking times, servings, ingredients, nutrition, instructions, and more. Recipe dataset is in csv format and it has 28 columns. The columns are ;
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

<b> The reviews dataset: </b> It contains 1,401,982 reviews from users. This dataset provides information about the author, rating, review text, and more. Reviews dataset is in parquet format and it has 8 columns. The columns are ;
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
After data exploration phase, I defined the conceptual data model as shown below.
<h3> 4-1 Staging Tables </h3>
The original datasets are in csv and parquet format. I created two Amazon Redshift tables in onder to store these original datasets. Recipes dataset is stored in staging_recipes table and reviews dataset is stored in staging_reviews table. Then I created an ETL processes to read and load original datasets into these Redshift tables. The detail of staging tables is below.<br><br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/staging_tables.jpg" style="float:left;vertical-align:bottom">

<h3> 4-2 Fact and Dimension Tables </h3>
I created five Redshift tables to store fact and dimension tables: These are reviews, recipes, author, time and category tables.<br>
<ul>
<li><b>Reviews: </b>This is the fact table in data model. It stores basic info about reviews and also foreign keys from other dimension tables.</li>
<li><b>Recipes: </b>This dimension table is for recipe data. Also it has RecipeCategoryId column from other dimension table.</li>
<li><b>Author: </b>I created author dimension table to store data about authors.</li>
<li><b>Time: </b>This is the time dimension table for storing submitted date of the reviews.</li>
<li><b>Category: </b>It is the dimension table to store category of recipes.</li>
</ul>
The whole conceptual data model is shown below.<br><br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/fact_dimension_tables.jpg">

<h2> 5- ETL Process </h2>
After defining the data model, it is time to create the ETL pipeline in order to feed all the tables in model. For this purpose, I created a well designed ETL pipeline in Apache Airflow. You can see the Airflow DAG Graph view below.<br><br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow.jpg">
<h3> ETL Steps </h3>
<ul>
<li><b>create_all_tables: </b> It creates all the tables in Redshift.</li>
<li><b>stage_reviews_to_redshift, stage_recipes_to_redshift :</b> They read and load original datasets into Redshift staging tables.</li>
<li><b>load_reviews_table :</b> It loads reviews fact table.</li>
<li><b>load_author_dimension_table, load_time_dimension_table, load_category_dimension_table, load_recipes_dimension_table :</b> They load four dimension tables.</li>
<li><b>run_quality_checks_author, run_quality_checks_recipes :</b> They check data quality issues in tables.</li>
</ul>
In the Airflow DAG Gantt View below, you can see the time takes for each step. As you noticed reading data from s3 bucket and loading it into staging tables takes longer than other steps in ETL because files in datasets are very big.<br><br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow_gantt.jpg"><br>
After ETL runs once, this is the Airflow DAG Tree view.<br><br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/airflow_tree.jpg"><br>
After the whole ETL process is finished, you can see the created tables in Redshift below.<br><br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/s3.jpg">

<h2> 6- About the Project </h2>
The main goal of this project was to create a good data model from various datasets and also build a good ETL pipeline end to end. I prefered to use Airflow as ETL scheduler, S3 as file storage and Redshift as relational database. The high level architecture diagram of the project is below. <br>
<img src="https://github.com/lemarc58/udacity/blob/main/image/architecture.jpg"> <br>
I choosed S3 and Redshift because both of them run on cloud and they have the ability of scaling up. Airflow is the most used Python based ETL scheduler tool and I used it in project.

<br><br>

<b>Project Directory</b><br>
<b>create_all_tables.sql =></b> sql queries for creating staging, fact and dimension tables <br>
<b>udacity_capstone_project_dag.py =></b> main dag file <br>
<b>sql_queries.py =></b> sql queries for inserting data into tables <br>
<b>data_quality.py =></b> check data quality operator file <br>
<b>load_dimension.py =></b> load dimension tables operator file <br>
<b>load_fact.py =></b> load fact table operator file <br>
<b>stage_redshift.py =></b> load staging tables operator file

<b>How to run project</b>
<ol>
<li>Be sure that Airflow is up and running </li>
<li>Save datasets in s3 bucket </li>
<li>Create AWS and Redshift connections in Airflow </li>
<li>Run DAG </li>
<li>Control every step in DAG and tables in Redshift </li>
</ol>

<h2> 7- Possible Scenarios </h2>
<ul>
  <li><b>If the data was increased by 100x. =></b> In this case, I would prefer to use Spark on Amazon EMR Cluster. Because it has high processing capability.</li>
  <li><b>If the pipelines were run on a daily basis by 7am. =></b> It is enough to change schedule_interval value and set it to daily 7 am in Airflow.</li>
  <li><b>If the database needed to be accessed by 100+ people. =></b> Amazon Redshift has enough resource to serve for many people but in case of any performance issues, I can scale up Redshift cluster. </li>
</ul>		
<br><br>
