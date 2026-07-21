# 1. Get a five-digit integer from the user
# 2. Extract each digit using floor division (//) and remainder (%) operators
# 3. Print the digits separated by three spaces each

number = int(input("Enter a five-digit integer: "))

digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

print(digit1, digit2, digit3, digit4, digit5, sep='   ')

