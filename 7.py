df_consultation['medicine_count'] = df_consultation['medicines'].apply(len)
average_medicines = df_consultation['medicine_count'].mean()
print(round(average_medicines, 2)) 
