def is_valid_mobile(number):
    if isinstance(number, str):
        # Remove prefix '+91' or '91'
        if number.startswith('+91'):
            number = number[3:]
        elif number.startswith('91'):
            number = number[2:]
        
        # Check if the remaining number is between 6000000000 and 9999999999
        if len(number) == 10 and number.isdigit() and 6000000000 <= int(number) <= 9999999999:
            return True
    return False

# Apply validation function
df_patient['isValidMobile'] = df_patient['phoneNumber'].apply(is_valid_mobile)

# Count valid phone numbers
valid_phone_count = df_patient['isValidMobile'].sum()
print(valid_phone_count) 
