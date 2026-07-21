# Ask the user for their age
age = int(input("Enter your age: "))

# Determine ticket price based on age groups
if age < 5:
    price = "Free"
elif age <= 12:
    price = "$5"
elif age <= 64:
    price = "$12"
else:
    price = "$8"

# Print the final price
print(f"Ticket Price: {price}")

