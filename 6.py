from datetime import datetime

# Calculate age from birthDate
current_year = datetime.now().year
df['age'] = df['patientDetails.birthDate'].dropna().apply(lambda x: current_year - int(x[:4]) if pd.notnull(x) else None)

# Define age group categorization
def categorize_age(age):
    if pd.isnull(age):
        return None
    elif age <= 12:
        return 'Child'
    elif age <= 19:
        return 'Teen'
    elif age <= 59:
        return 'Adult'
    else:
        return 'Senior'

# Create the ageGroup column
df['ageGroup'] = df['age'].apply(categorize_age)

# Count of 'Adult'
adult_count = df['ageGroup'].value_counts().get('Adult', 0)
adult_count
