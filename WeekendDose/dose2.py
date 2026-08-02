numbers = int(input("Enter number n: "))
result = 1

for number in range(1, numbers + 1):
    result *= number

print("The factorial of the number is:", result)

