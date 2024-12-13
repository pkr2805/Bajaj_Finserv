import pandas as pd
import json

# Load JSON data
file_path = '/mnt/data/DataEngineeringQ2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract patientDetails and consultationData
patient_details = [entry['patientDetails'] for entry in data]
consultation_data = [{'appointmentId': entry['appointmentId'], 'medicines': entry['consultationData']['medicines']} for entry in data]

# Create DataFrames for patientDetails and consultationData
df_patient = pd.DataFrame(patient_details)
df_consultation = pd.DataFrame(consultation_data)

# Inspect the DataFrames
print("Patient Details DataFrame:")
print(df_patient.head())
print("\nConsultation Data DataFrame:")
print(df_consultation.head())
