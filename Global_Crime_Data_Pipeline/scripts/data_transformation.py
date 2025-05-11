from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace
import pandas as pd
import os

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("DataTransformation") \
    .getOrCreate()

# File paths
input_file = '../data/raw/crime_data.csv'
output_file = '../data/processed/cleaned_crime_data.csv'

# Check if the file exists
if not os.path.exists(input_file):
    print("Source file not found. Please run the data_ingestion.py script first.")
else:
    print("Source file found. Starting transformation...")

    # Load the raw data
    df = spark.read.csv(input_file, header=True, inferSchema=True)
    
    # Display initial schema and data
    print("Schema before Transformation:")
    df.printSchema()
    df.show(5)

    # Data Cleaning and Transformation
    # Removing unwanted characters from 'location' column
    df = df.withColumn('location', regexp_replace('location', '[^a-zA-Z0-9 ]', ''))
    
    # Drop duplicates and handle missing values
    df = df.dropDuplicates()
    df = df.na.fill({'location': 'Unknown', 'crime_type': 'Not Specified'})

    # Show transformed data
    print("Schema after Transformation:")
    df.printSchema()
    df.show(5)

    # Save the transformed data
    os.makedirs('../data/processed/', exist_ok=True)
    df.toPandas().to_csv(output_file, index=False)
    print(f"Data Transformation Completed. File saved to {output_file}")

