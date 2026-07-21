# Prompt for and input the user's age
age = int(input("Enter your age in years: "))

# Calculate maximum heart rate
max_heart_rate = 220 - age

# Calculate target heart rate range (50% to 85%)
target_min = max_heart_rate * 0.50
target_max = max_heart_rate * 0.85

# Display the calculated metrics
print(f"\nYour maximum heart rate is: {max_heart_rate} bpm")
print(f"Your target heart rate range is: {target_min:.1f} - {target_max:.1f} bpm")

