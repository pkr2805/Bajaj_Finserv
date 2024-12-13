import pandas as pd
import json

# Load the JSON data
file_path = '/mnt/data/DataEngineeringQ2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert JSON to DataFrame
df = pd.json_normalize(data, sep=".")

# Columns to check for missing values
columns_to_check = ['patientDetails.firstName', 'patientDetails.lastName', 'patientDetails.birthDate']

# Calculate missing value percentage for the specified columns
missing_percentage = {
    col: round((df[col].isnull() | (df[col] == '')).mean() * 100, 2) for col in columns_to_check
}

missing_percentage
