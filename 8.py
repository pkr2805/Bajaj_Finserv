all_medicines = [medicine['medicineName'] for entry in data for medicine in entry['consultationData']['medicines']]

# Count frequency of each medicineName
medicine_frequency = pd.Series(all_medicines).value_counts()
third_most_frequent = medicine_frequency.index[2]
print(third_most_frequent)
