numbers = int(input("Enter number n: "))
print(" Multiplication Table ")

for number in range(1, 11):
    multiply = numbers * number
    print(f"{numbers} x {number} = {multiply}")

