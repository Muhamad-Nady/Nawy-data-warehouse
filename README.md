# Nawy Data Warehouse
## Nawy Data Warehouse is a project aimed at storing and analyzing real estate data. The following steps outline the data pipeline implemented in this project.

## Nawy data warehouse is a project where I store and anlyize

![Nawy drawio](https://github.com/Muhamad-Nady/Nawy-data-warehouse/assets/34611160/9b60df22-b5ac-4247-82a2-84e24a622b97)

## Project Pipeline
### 1. Ingest Data
#### Utilize a Python scraper script to extract data.
#### Save the extracted data in CSV files: [container_data.csv, units_data.csv].
### 2. Data Validation
#### Implement data validation procedures to ensure the quality and integrity of the dataset.
### 3. Data Transformation
#### Split the data into five tables for insertion into the data warehouse tables:
#### 'area'
#### 'compounds'
#### 'property'
#### 'developer'
#### 'property_type'
#### 'property_type_count'
### 4. Database Environment
#### Set up a database environment using the docker-compose file.
### 5. Connect to Database Server
#### Establish a connection to the database server using Python.
### 6. ETL Process
#### Perform the Extract, Transform, Load (ETL) process to populate the data warehouse schema.
### 7. Business Insights
#### Connect the analysis.py file to the database engine.
### Extract business insights and perform data analysis.
