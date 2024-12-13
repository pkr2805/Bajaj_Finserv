
gender_column = 'patientDetails.gender'
mode_gender = df[gender_column][df[gender_column] != ''].mode().iloc[0]


df[gender_column] = df[gender_column].replace('', pd.NA).fillna(mode_gender)


female_percentage = round((df[gender_column] == 'F').mean() * 100, 2)

