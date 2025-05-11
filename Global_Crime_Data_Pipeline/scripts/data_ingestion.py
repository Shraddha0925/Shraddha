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
ex
