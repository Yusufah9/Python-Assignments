# Input three floating-point numbers
# Compare and swap variables step-by-step
# Display the sorted numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


if num1 > num2:
    num1, num2 = num2, num1  
if num1 > num3:
    num1, num3 = num3, num1  
if num2 > num3:
    num2, num3 = num3, num2 


print(f"Numbers in increasing order: {num1}, {num2}, {num3}")

