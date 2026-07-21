from functools import reduce
import operator

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

numbers = [num1, num2, num3]

total_sum = sum(numbers)
average   = total_sum / len(numbers)
product   = reduce(operator.mul, numbers)
smallest  = min(numbers)
largest   = max(numbers)

print(f"\nResults:")
print(f"Sum:      {total_sum}")
print(f"Average:  {average:.2f}")
print(f"Product:  {product}")
print(f"Smallest: {smallest}")
print(f"Largest:  {largest}")

