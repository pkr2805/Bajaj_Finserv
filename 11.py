from datetime import datetime

current_year = datetime.now().year
df_patient['birthDate'] = pd.to_datetime(df_patient['birthDate'], errors='coerce')
df_patient['age'] = current_year - df_patient['birthDate'].dt.year


df_consultation['medicine_count'] = df_consultation['medicines'].apply(len)

df_combined = df_patient.merge(df_consultation, left_on='_id', right_on='_id', how='inner')

correlation = df_combined['medicine_count'].corr(df_combined['age'])
print(round(correlation, 2)) 
