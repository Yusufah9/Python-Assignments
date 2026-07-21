# Ask the user for two integers
# Check if denominator is zero before dividing

x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))

if y != 0:
    result = x / y
    print(f"Result: {result}")
else:
    print("Cannot divide by zero")

