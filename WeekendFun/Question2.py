
a = int(input("Enter first integer (a): "))
b = int(input("Enter second integer (b): "))
c = int(input("Enter third integer (c): "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

# Print the result
print(f"The largest number is: {largest}")

