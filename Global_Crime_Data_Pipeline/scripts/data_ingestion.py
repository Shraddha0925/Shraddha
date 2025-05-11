import requests
import pandas as pd
import yaml
import os
from datetime import datetime

# Create a log file to store the output
log_file = '../logs/data_ingestion_log.txt'
os.makedirs('../logs/', exist_ok=True)

def log_message(message):
    with open(log_file, 'a') as log:
        log.write(f"{datetime.now()} - {message}\n")
    print(message)

# Load configurations
try:
    with open('../configs/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    log_message("Configurations loaded successfully.")
except Exception as e:
    log_message(f"Error loading configurations: {e}")

# API Endpoint
url = config.get('api_endpoint', '')

# Fetch Data
log_message("Fetching data from API...")
response = requests.get(url)

if response.status_code == 200:
    log_message("Data fetched successfully!")
    data = response.json()
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Create directory if not exists
    os.makedirs('../data/raw/', exist_ok=True)
    
    # Save to CSV
os.makedirs('../data/raw/', exist_ok=True)
df.to_csv('Global_Crime_Data_Pipeline/scripts/crime_data.csv', index=False)
print("Data saved to scripts/crime_data.csv")

    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")

