# Nawy Data Warehouse

## Nawy Data Warehouse is a project aimed at storing and analyzing real estate data. The following steps outline the data pipeline implemented in this project.
![Nawy drawio](https://github.com/Muhamad-Nady/Nawy-data-warehouse/assets/34611160/9b60df22-b5ac-4247-82a2-84e24a622b97)

## Project Pipeline
### 1. Ingest Data
#### - Utilize a Python scraper script to extract data.
#### - Save the extracted data in CSV files: [container_data.csv, units_data.csv].
### 2. Data Validation
#### - Implement data validation procedures to ensure the quality and integrity of the dataset.
### 3. Data Transformation
#### Split the data into five tables for insertion into the data warehouse tables:
#### - ['area', 'compounds', 'property', 'developer', 'property_type', 'property_type_count']
### 4. Database Environment
#### - Set up a database environment using the docker-compose file.
### 5. Connect to Database Server
#### - Establish a connection to the database server using Python.
### 6. ETL Process
#### - Perform the Extract, Transform, Load (ETL) process to populate the data warehouse schema.
### 7. Business Insights
#### - Connect the analysis.py file to the database engine.
#### - Extract business insights and perform data analysis.



## project implementation steps
### Data Scraping:
#### - Utilize the curl command for JSON back-end fetch requests in Python.
#### - Code can be found in the "Scraping_code" directory.

### Docker Compose:
#### - Create a Docker Compose file in the "Docker" directory to build and run "PostgreSQL database and pgAdmin" services.

### Database Schema:
#### - Develop a database schema from the extracted data.
#### - Include the .sql DDL file in the "Schema" directory.

### Data Validation:
#### - Implement data validation processes before transforming and loading data into the database.
#### - Code can be found in the "Data_validation" directory.

### ETL (Extract, Transform, Load):
#### - Read the extracted data as a Pandas dataframe.
#### - Perform data transformation and load data into database tables.
#### - Code is located in the "ETL" folder.

### Business Insights:
#### - Connect to the database, extract relevant business insights.
#### - Find insights in the "Insights" directory.
