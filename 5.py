# Impute missing 'gender' values with the mode
gender_column = 'patientDetails.gender'
mode_gender = df[gender_column][df[gender_column] != ''].mode().iloc[0]

# Fill missing or empty values in the gender column with the mode
df[gender_column] = df[gender_column].replace('', pd.NA).fillna(mode_gender)

# Calculate the percentage of 'F' (Female) after imputation
female_percentage = round((df[gender_column] == 'F').mean() * 100, 2)
female_percentage
