import requests
import pandas as pd
import yaml
import os

# Load configurations
with open('../configs/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# API Endpoint
url = config['api_endpoint']

# Fetch Data
print("Fetching data from API...")
response = requests.get(url)

if response.status_code == 200:
    print("Data fetched successfully!")
    data = response.json()
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Create directory if not exists
    os.makedirs('../data/raw/', exist_ok=True)
    
    # Save to CSV
    df.to_csv('../data/raw/crime_data.csv', index=False)
    print("Data saved to data/raw/crime_data.csv")
else:
    print("Failed to fetch data. Status Code:", response.status_code)

