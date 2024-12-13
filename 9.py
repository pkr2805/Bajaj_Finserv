active_count = sum(med['isActive'] for entry in data for med in entry['consultationData']['medicines'])
inactive_count = sum(not med['isActive'] for entry in data for med in entry['consultationData']['medicines'])

# Calculate percentages
total_count = active_count + inactive_count
active_percentage = (active_count / total_count) * 100
inactive_percentage = (inactive_count / total_count) * 100
print(round(active_percentage, 1), round(inactive_percentage, 1))
